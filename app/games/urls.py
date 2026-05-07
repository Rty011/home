from django.urls import path
from . import views

urlpatterns = [
    path('v1/games/list-games/', views.list_games, name='list_games'),
    path('v1/games/game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('v1/games/list-genres/', views.list_genres, name='list_genres'),
]