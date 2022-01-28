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
    
    reco_params = {'api_key':'7f292cc09a9aff763e3e54a81c1ec05a', 'language':'ko','page':'',}
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
