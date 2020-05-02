from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('updateduty/<str:pk>/', views.updateDuty, name="update"),
    path('deleteduty/<str:pk>/', views.deleteDuty, name="delete"),
]
