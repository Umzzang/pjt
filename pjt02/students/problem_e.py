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
