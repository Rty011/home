from django.urls import path
from . import views

urlpatterns = [
    path('api/greeting/', views.greeting, name='greeting'),
    path('api/about/', views.about_us, name='about_us'),
    path('api/contacts/', views.contacts, name='contacts'),
]