import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()
rows = rjson['RealtimeCityAir']['row']

for row in rows:
    name = row['MSRSTE_NM']
    dust = row['IDEX_MVL']
    if dust < 60:
        print(name)