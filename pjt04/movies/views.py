from django.shortcuts import render
import requests
import random
# Create your views here.

def index(request):
    context = {
        'movies' : [{'title':f'제목{i}', 'content' : f'내용{i}'} for i in range(1,7)]
    }
    
    return render(request, 'movies/index.html', context)


def recommendations(request):
    url = 'https://api.themoviedb.org/3/movie/278/recommendations'
    param={
        'api_key' : '7f292cc09a9aff763e3e54a81c1ec05a',
        'region': 'KR',
        'language': 'ko'
    }
    res = requests.get(url, params=param).json()
    movie = random.choice(res.get('results'))
    pic = 'https://image.tmdb.org/t/p/w500'
    path = movie.get('poster_path')
    picture = pic + path
    overview = movie.get('overview')
    title = movie.get('title')
    vote_average = round(movie.get('vote_average'),1)
    release_date = movie.get('release_date')
    context = {
        'res' : res,
        'movie' : movie,
        'pic' : pic,
        'path' : path,
        'picture' : picture,
        'overview' : overview,
        'title' : title,
        'release_date' : release_date,
        'vote_average' : vote_average
    }
    return render(request,'movies/recommendations.html', context)