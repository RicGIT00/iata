from django.urls import path

from . import views

urlpatterns = [
    path('jobs-rh', views.vacanciesJob, name='jobs-rh'),
    path('job-form', views.createJobVacancy, name='job-form'),
    path('createJobVacancy', views.createJobVacancy, name='createJobVacancy')
]
