from django.shortcuts import render, get_object_or_404
from .models import Movie

def home(request):
    featured_movies = Movie.objects.filter(is_featured=True)
    all_movies = Movie.objects.all()
    action_movies = Movie.objects.filter(genre__icontains='Action')
    animation_movies = Movie.objects.filter(genre__icontains='Animation')
    
    context = {
        'featured_movies': featured_movies,
        'all_movies': all_movies,
        'action_movies': action_movies,
        'animation_movies': animation_movies,
    }
    return render(request, 'home.html', context)

def play_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'play.html', {'movie': movie})
    def play real world (100*80)
    jawan 2026 ( 10080 hd )
    pathan 2026 (10080 hd )
    bajrangi baijaan (10080 hd)
    should by emiter could by sound him real 
    What is so poor network to internet canecation 
    That main has power backup by high edvantage 
    Cool by thourgo has been done by city
    Has to manage by bangolore has center by infosys 
    Super corridor , NH 45 by Indore 
    Infosys Campus 
