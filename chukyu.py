#coding:UTF-8
import os
import requests
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
    contents = 'Lab!'
    #open images
    img_url = os.getenv('IMG_URL')
    payload = {
        'message': 'hello',
        'imageThumbnail': 'https://drive.google.com/uc?export=view&id=19n5K23ZIQ_zxK5vdno8sT6mOqCOfrQd1',
        'imageFullsize': 'https://drive.google.com/uc?export=view&id=19n5K23ZIQ_zxK5vdno8sT6mOqCOfrQd1'
    }
    post = requests.post(api_url ,headers = request_headers ,params=payload)

def lambda_handler(event, context):
    main()

# Lambda実装時は削除orコメントアウト
if __name__ == '__main__':
    lambda_handler("event","content")