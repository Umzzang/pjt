import requests
from pprint import pprint


def ranking():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {'api_key':'7f292cc09a9aff763e3e54a81c1ec05a',  'language':'ko', 'page': '', 'region' : 'KR'}
    response = requests.get(BASE_URL+path, params=params).json()
    max5_list = []
    vote_list = []
    for i in range(len(response['results'])):
        vote_list += [response['results'][i]['vote_average']]

    vote_list.sort()
    vote_list.reverse()
    j = 0
    while j < 5:
        for i in range(len(response['results'])):
            if response['results'][i]['vote_average'] == vote_list[j]:
                max5_list += [response['results'][i]]
                j += 1

        


    return max5_list


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
