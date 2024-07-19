#coding:UTF-8
import os
import urllib.request
from dotenv import load_dotenv

load_dotenv() # .envファイルの読み込み
token = os.getenv('TOKEN') # Tokenを読み込み(Lambda実装時は別の方法で環境変数を取ってくる)

api_url = 'https://notify-api.line.me/api/notify' # APIのURL

# リクエストのヘッダーを定義
request_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + token
}

def main():
    # data引数はbytes型を期待しているためbytes型に変換
    contents = 'テスト from lambda'
    payload = {'message': contents}
    data = urllib.parse.urlencode(payload).encode('ascii')
    req = urllib.request.Request(api_url, headers=request_headers, data=data, method='POST')
    conn = urllib.request.urlopen(req)

def lambda_handler(event, context):
    main()

# Lambda実装時は削除orコメントアウト
if __name__ == '__main__':
    lambda_handler("event","content")