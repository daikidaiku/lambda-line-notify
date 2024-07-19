#coding:UTF-8
import urllib.request
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv() # .envファイルの読み込み
token = os.getenv('TOKEN') # Tokenを読み込み(Lambda実装時は別の方法で環境変数を取ってくる)
api_url = 'https://notify-api.line.me/api/notify' # APIのURL

# リクエストのヘッダーを定義
request_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + token
}

# 町田市の天気を取得
def get_weather():
    info = requests.get("https://tenki.jp/forecast/3/16/4410/13209/") # レスポンス
    bs = BeautifulSoup(info.content, "html.parser") # Webページの内容
    
    today = bs.find(class_="today-weather") # classが"today-weather"であるHTMLタグを検索
    
    h2_tag = bs.find("h2").text # h2タグを検索
    
    idx = h2_tag.find("の天気") # "の天気"のインデックス
    
    location = h2_tag[0:idx+3] # "◯◯市の天気"
    
    # 天気、最高気温、最低気温をstrとして抽出
    weather = today.find(class_="weather-telop").string # 天気
    high_temp = today.find_all(class_="value")[0].string # 最高気温
    low_temp = today.find_all(class_="value")[1].string # 最低気温
    
    message = "今日の"  + location + "は" + weather + "、最高気温は{}℃".format(high_temp) + "、最低気温は{}℃です。".format(low_temp)
    return message

def main():
    contents = get_weather()
    payload = {'message': contents}
    data = urllib.parse.urlencode(payload).encode('ascii')
    req = urllib.request.Request(api_url, headers=request_headers, data=data, method='POST')
    conn = urllib.request.urlopen(req)

def lambda_handler(event, context):
    main()

# Lambda実装時は削除orコメントアウト
if __name__ == '__main__':
    lambda_handler("event","content")