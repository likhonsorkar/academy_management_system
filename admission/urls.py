
from django.contrib import admin
from django.urls import path
from core.views import index
from . import views

urlpatterns = [
    path('', views.admission_create, name='admission'),
    path('payment/<uuid:admission_id>/', views.submit_payment, name='payment'),
    path('find-admission-id/', views.find_admission_id, name='find_admission_id'),
    path('status/', views.check_status, name='status'),
]
