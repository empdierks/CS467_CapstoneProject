from django.urls import path
from capstone_app import views

urlpatterns = [
    path('', views.index, name='main'),
]
