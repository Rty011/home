from django.shortcuts import render
from django.http import JsonResponse
from .models import Games, Genre

# Create your views here.

def list_games(request):
    """API endpoint for games list"""
    games = Games.objects.all()
    games_list = []
    
    for game in games:
        games_list.append({
            'id': game.id,
            'title': game.title,
            'description': game.description,
            'price': float(game.price),
            'release_data': game.release_data,
            'developer': game.developer,
            'rating': game.rating,
            'genre': game.genre.name if game.genre else None,
            'image': game.image.url if game.image else None,
            'created_at': game.created_at.isoformat()
        })
    
    return JsonResponse({
        'games': games_list,
        'count': len(games_list),
        'status': 'success'
    })

def game_detail(request, game_id):
    """API endpoint для детальной информации об игре"""
    try:
        game = Games.objects.get(id=game_id)
        
        game_data = {
            'id': game.id,
            'title': game.title,
            'description': game.description,
            'price': float(game.price),
            'release_data': game.release_data,
            'developer': game.developer,
            'rating': game.rating,
            'genre': {
                'id': game.genre.id,
                'name': game.genre.name
            } if game.genre else None,
            'image': game.image.url if game.image else None,
            'created_at': game.created_at.isoformat()
        }
        
        return JsonResponse({
            'game': game_data,
            'status': 'success'
        })
    
    except Games.DoesNotExist:
        return JsonResponse({
            'error': 'Game not found',
            'status': 'error'
        }, status=404)

def list_genres(request):
    """API endpoint для списка жанров"""
    genres = Genre.objects.all()
    genres_list = []
    
    for genre in genres:
        genres_list.append({
            'id': genre.id,
            'name': genre.name,
            'slug': genre.slug
        })
    
    return JsonResponse({
        'genres': genres_list,
        'count': len(genres_list),
        'status': 'success'
    })