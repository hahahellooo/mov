import requests
import os
import pandas as pd


def save2df():
    df = list2df()
    # df 에 ldad_dt 컬럼 추가 (조회 일자 YYYYMMDD 형식으로)
    # 아래 파일 저장시 load_dt 기준으로 파티셔닝
    df['load_dt'] = '20120101'
    df.to_parquet('~/tmp/test_parquet', partition_cols=['load_dt'])
    print(df.head(5))
    return df

def list2df():
    l = req2list()
    df = pd.DataFrame(l)
    return df

def req2list():
    _, data = req()
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def get_key():
    """영화진흥위원회 가입 및 API 키 생성 후 환경 변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(dt="20120101"):
    url = gen_url(dt)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    print(data)
    return code, data


def gen_url(dt="20120101"):
    base_url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
#호출방법
#req()
#req("8"*8)
#req(dt="99999999999999999")

    return url


