"""Arike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user.views import (
    HomeView,
    UserCreateView,
    log_in,
    UserLoginView,
    CreatePatientView,
    DeletePatientView,
    UpdatePatientView,
    DetailPatientView,
    #GenericDashboardView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view()),
    path("login/", log_in, name='login'),
    path("signup/", UserCreateView.as_view()),
    path("patient-create",CreatePatientView.as_view()),
    path("patient-delete/<pk>",DeletePatientView.as_view()),
    path("patient-update/<pk>",UpdatePatientView.as_view()),
    path("patient-detail/<pk>",DetailPatientView.as_view()),

    # path("dashboard/", GenericDashboardView.as_view()),
]
