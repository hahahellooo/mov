def req(dt="20120101"):
    base_url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "6b328d3bbd3cef67be8ac18f563a84e0"
    url = f"{base_url}?key={key}&targetDt={dt}"
    print(url)
#호출방법
#req()
#req("8"*8)
#req(dt="99999999999999999")

