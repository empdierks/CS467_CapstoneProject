from django.urls import path
from capstone_app import views

urlpatterns = [
    path('', views.index, name='main'),
    path('retrieveData/', views.post_models, name='data')
]
