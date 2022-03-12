from cProfile import run
from configparser import SectionProxy
import datetime
import email
import time

from django.core.mail import send_mail
from user.models import FamilyDetails, User, VisitDetails, VisitSchedule
from datetime import timedelta

from celery.decorators import periodic_task

from Arike.celery import app

def user_created_email(user):
    try:
        send_mail(
            "User Created",
            f"email:{user.email} password:primarynurse",
            "qwe@qwe.com",
            [user.email],
        )
        user.isFirst = False
    except:
        user.isFirst = True
    user.save()

@periodic_task(run_every=timedelta(seconds=30))
def every_30_seconds():
    print("Running Every 30 Seconds!")
    return True

@periodic_task(run_every=timedelta(seconds=30))
def daily_report_email():
    now_time = datetime.datetime.now()
    now_date = datetime.date.today()
    default_report_time = datetime.time(9,00)
    users = User.objects.filter(role='primary_nurse',last_email_sent_date__lte = now_date - timedelta(days=1))
    for user in users:
        visit_schedule_count = VisitSchedule.objects.filter(date__range =[ now_time - timedelta(days=1),now_time]).count()
        try:
            send_mail(
                "Treatment Report",
                f"no of treated patients are {visit_schedule_count}",
                "qwe@qwe.com",
                [user.email],
            )
            user.last_email_sent_date = now_date
        except:
            pass
        user.save()

@periodic_task(run_every=timedelta(seconds=30))
def visit_mail():
    visit_schedules = VisitSchedule.objects.filter(email_sent = False,date__lte=datetime.datetime.now())
    for visit_schedule in visit_schedules:
        patient = visit_schedule.patient
        families = FamilyDetails.objects.filter(patient=patient)
        details = VisitDetails.objects.filter(visit_schedule=visit_schedule)
        totaldetail = ""
        for detail in details:
            totaldetail += detail
        for family in families:
            try:
                send_mail(
                    "Patient Status",
                    totaldetail,
                    "qwe@qwe.com",
                    [family.email],
                )
                visit_schedule.email_sent = True
            except:
                visit_schedule.email_sent = False
            visit_schedule.save()