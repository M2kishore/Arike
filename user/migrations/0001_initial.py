# Generated by Django 4.0.3 on 2022-03-04 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icds_code', models.CharField(choices=[('D-32', 'DM'), ('HT-58', 'Hypertension'), ('IHD-21', 'IDH'), ('DPOC-144', 'COPD'), ('DM-62', 'Dementia'), ('CVA-89', 'CVA'), ('C-98', 'Cancer'), ('DC-225', 'CKD')], default='D-32', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LgsBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[(1, 'Grama Panchayath'), (2, 'Block Panchayath'), (3, 'District Panchayath'), (4, 'Nagar Panchayath'), (10, 'Municipality'), (20, 'Corporation'), (50, 'Others')], default=1, max_length=100)),
                ('lsg_body_code', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.district')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('landmark', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), (3, 'Non_Binary')], default='Male', max_length=100)),
                ('emergency_phone_number', models.IntegerField()),
                ('expired_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('care_type', models.CharField(choices=[('GENERAL_CARE', 'GENERAL_CARE'), ('GENITO_URINARY_CARE', 'GENITO_URINARY_CARE'), ('GASTRO_INTESTINAL_CARE', 'GASTRO_INTESTINAL_CARE'), ('WOUND_CARE', 'WOUND_CARE'), ('RESPIRATORY_CARE', 'RESPIRATORY_CARE')], default='GENERAL_CARE', max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('primary_nurse', 'primary_nurse'), ('secondary_nurse', 'secondary_nurse'), ('district_admin', 'district_admin')], default='primary_nurse', max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('is_verified', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('lgs_body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.lgsbody')),
            ],
        ),
        migrations.CreateModel(
            name='VisitSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.patient')),
            ],
        ),
        migrations.CreateModel(
            name='VisitDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pallivative_phase', models.CharField(choices=[('STABLE', 'STABLE'), ('UNSTABLE', 'USTABLE'), ('DETORIATING', 'DETORIATING'), ('TERMINAL', 'TERMINAL'), ('BEREAVEMENT', 'BEREAVEMENT')], default='STABLE', max_length=100)),
                ('blood_pressure', models.IntegerField()),
                ('pulse', models.IntegerField()),
                ('general_random_blood_sugar', models.IntegerField()),
                ('personal_hygine', models.CharField(max_length=10)),
                ('mouth_hygine', models.CharField(max_length=100)),
                ('public_hygine', models.CharField(max_length=100)),
                ('systemic_examination', models.CharField(max_length=100)),
                ('patient_at_peace', models.BooleanField(default=True)),
                ('pain', models.BooleanField(default=True)),
                ('symptoms', models.CharField(choices=[('NONE', 'NONE'), ('HEADACHE', 'HEADACHE'), ('STOMACHACHE', 'STOMACHACHE'), ('VOMITING', 'VOMITING'), ('CHESTPAIN', 'CHESTPAIN')], default='NONE', max_length=100)),
                ('note', models.CharField(max_length=255)),
                ('visit_schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.visitschedule')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=255)),
                ('describe', models.CharField(max_length=255)),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.treatment')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.visitdetails')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=255)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.disease')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.ward'),
        ),
        migrations.CreateModel(
            name='FamilyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('relation', models.CharField(choices=[('OTHER', 'OTHER'), ('BROTHER', 'BROTHER'), ('FATHER', 'FATHER'), ('MOTHER', 'MOTHER'), ('SON', 'SON'), ('DAUGHTER', 'DAUGHTER'), ('GRAND_FATHER', 'GRAND_FATHER'), ('GRAND_MOTHER', 'GRAND_MOTHER'), ('GUARDIAN', 'GURDIAN')], default='OTHER', max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=255)),
                ('is_primary', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('PHC', 'PHC'), ('CHC', 'CHC')], default='PHC', max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('pincode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('ward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.ward')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.state'),
        ),
    ]
