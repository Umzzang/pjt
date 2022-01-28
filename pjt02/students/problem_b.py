import requests
from pprint import pprint


def vote_average_movies():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {'api_key' : '7f292cc09a9aff763e3e54a81c1ec05a', 'language' : 'ko', 'page':'', 'region' : 'KR'}
    movie_list = []
    response = requests.get(BASE_URL+path, params= params).json()
    for i in range(len(response['results'])):
        if response['results'][i]['vote_average'] >= 8:
            movie_list += [response['results'][i]]
    return movie_list


if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
