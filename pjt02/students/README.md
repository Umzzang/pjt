# 1. problem_a

```python
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

```

```
20
```



# 2. problem_b

```python
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

```

```markdown
[{'adult': False,
  'backdrop_path': '/iQFcwSGbZXMkeyKrxbPnwnRo5fl.jpg',
  'genre_ids': [28, 12, 878],
  'id': 634649,
  'original_language': 'en',
  'original_title': 'Spider-Man: No Way Home',
  'overview': '정체가 탄로난 스파이더맨 피터 파커가 시간을 되돌리기 위해 닥터 스트레인지의 도움을 받던 중 뜻하지 않게 '
              '멀티버스가 열리게 되고, 이를 통해 자신의 숙적 닥터 옥토퍼스가 나타나며 사상 최악의 위기를 맞게 되는데...',
  'popularity': 18473.631,
  'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
  'release_date': '2021-12-15',
  'title': '스파이더맨: 노 웨이 홈',
  'video': False,
  'vote_average': 8.5,
  'vote_count': 6194},
 {'adult': False,
  'backdrop_path': '/tutaKitJJIaqZPyMz7rxrhb4Yxm.jpg'
  .
  .
  .
```





# 3. problem_c

```python
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

```

```markdown
[{'adult': False,
  'backdrop_path': '/iQFcwSGbZXMkeyKrxbPnwnRo5fl.jpg',
  'genre_ids': [28, 12, 878],
  'id': 634649,
  'original_language': 'en',
  'original_title': 'Spider-Man: No Way Home',
  'overview': '정체가 탄로난 스파이더맨 피터 파커가 시간을 되돌리기 위해 닥터 스트레인지의 도움을 받던 중 뜻하지 않게 '
              '멀티버스가 열리게 되고, 이를 통해 자신의 숙적 닥터 옥토퍼스가 나타나며 사상 최악의 위기를 맞게 되는데...',       
  'popularity': 18473.631,
  'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
  'release_date': '2021-12-15',
  'title': '스파이더맨: 노 웨이 홈',
  'video': False,
  'vote_average': 8.5,
  'vote_count': 6194},
 {'adult': False,
  'backdrop_path': '/xPpXYnCWfjkt3zzE0dpCNME1pXF.jpg',
  'genre_ids': [16, 28, 12, 14],
  'id': 635302,
  'original_language': 'ja',
  'original_title': '劇場版「鬼滅の刃」無限列車編',
  .
  .
  .
```







# 4. problem_d

```python
import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {'api_key':'7f292cc09a9aff763e3e54a81c1ec05a', 'language':'ko', 'query':title }
    response = requests.get(BASE_URL+path, params=params).json()
    response_url = requests.get(BASE_URL+path, params=params).url
    
    try:
        id = response['results'][0]['id']
        
    except:
        return None

    RECOBASE_URL = 'https://api.themoviedb.org/3'
    reco_path = f'/movie/{id}/recommendations'
    
    reco_params = {'api_key':'7f292cc09a9aff763e3e54a81c1ec05a', 'language':'ko'}
    reco_response = requests.get(RECOBASE_URL + reco_path, params= reco_params).json()
    reco_url = requests.get(RECOBASE_URL + reco_path, params= reco_params).url

    name_list = []
    try:
        for i in range(len(reco_response)):
            name_list += [reco_response['results'][i]['title']]

        return name_list
    except:
        return name_list

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면.
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None

```

```markdown
['조커', '조조 래빗', '1917', '원스 어폰 어 타임 인… 할리우드']
[]
None
```







# 5. problem_e

```python
import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {'api_key':'7f292cc09a9aff763e3e54a81c1ec05a', 'language':'ko', 'query':title }
    response = requests.get(BASE_URL+path, params=params).json()
    response_url = requests.get(BASE_URL+path, params=params).url  
    try:
        id = response['results'][0]['id']
        
    except:
        return None

    cre_BASE_URL = 'https://api.themoviedb.org/3'
    cre_path = f'/movie/{id}/credits'
    cre_params = {'api_key':'7f292cc09a9aff763e3e54a81c1ec05a', 'language':'ko' }
    cre_response = requests.get(cre_BASE_URL + cre_path, params= cre_params).json()
    cre_response_url = requests.get(cre_BASE_URL + cre_path, params= cre_params).url

    actor_list = []
    direct_list =[]
    credit_dict = {}
    for i in range(len(cre_response['cast'])):
        if cre_response['cast'][i]['cast_id'] < 10:
            actor_list += [cre_response['cast'][i]['name']]
    
    for i in range(len(cre_response['crew'])):
        if cre_response['crew'][i]['department'] == 'Directing':
            direct_list += [cre_response['crew'][i]['name']]

    credit_dict['cast'] = actor_list
    credit_dict['crew'] = direct_list

    
    return credit_dict

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None

```

```markdown
{'cast': ['Song Kang-ho',
          'Lee Sun-kyun',
          'Cho Yeo-jeong',
          'Choi Woo-shik',
          'Park So-dam',
          'Lee Jung-eun',
          'Jang Hye-jin'],
 'crew': ['Bong Joon-ho',
          'Park Hyun-cheol',
          'Han Jin-won',
          'Kim Seong-sik',
          'Lee Jung-hoon',
          'Yoon Young-woo']}
None
```

