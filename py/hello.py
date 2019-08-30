# $ pip install requests ~> 외부 라이브러리 사용하기 요청
import requests
# url로 요청하여
url="https://api.bithumb.com/public/ticker/btc"
# 값을 받아온다.
response = requests.get(url).json()
print(response['data']['max_price'])