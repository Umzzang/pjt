import json
import requests 


def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {'api_key' : '7f292cc09a9aff763e3e54a81c1ec05a', 'language' : 'ko', 'page':'', 'region' : 'KR'}
    response = requests.get(BASE_URL+path, params= params).json()
    
    return len(response['results'])


popular_count()

if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
