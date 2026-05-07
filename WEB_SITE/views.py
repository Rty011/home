from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def greeting(request):
    """API endpoint для приветствия"""
    return JsonResponse({
        'message': 'Добро пожаловать в наш сайт!',
        'status': 'success'
    })

def about_us(request):
    """API endpoint для информации о нас"""
    return JsonResponse({
        'title': 'О нас',
        'description': 'Мы - компания, которая создает качественные веб-решения для наших клиентов.',
        'status': 'success'
    })

def contacts(request):
    """API endpoint для контактной информации"""
    return JsonResponse({
        'title': 'Контакты',
        'phone': '+996 700 00 00 00',
        'email': 'test@gmail.com',
        'status': 'success'
    })