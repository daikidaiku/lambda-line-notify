<p>
<img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat">
<img src="https://img.shields.io/badge/-Raspberry%20Pi-C51A4A.svg?logo=raspberry-pi&style=flat">
<img src="https://img.shields.io/badge/-Visual%20Studio%20Code-007ACC.svg?logo=visual-studio-code&style=flat">
<img src="https://img.shields.io/badge/-GitHub-181717.svg?logo=github&style=flat">
<img src="https://img.shields.io/badge/-AWS Lambda-FFFFFF.svg?logo=AWSLambda&style=flat">
</p>

# lab-detection<!-- TODO 書く -->
LINE NotifyによりLINEにテキストや写真を通知するPythonコードです。
AWSのLambdaへの実装を想定しています。

# DEMO
```mermaid
flowchart TD
    subgraph AWS Lambda
        A[shokyu.py]
        B[chukyu.py]
        C[jokyu.py]
    end
    A --> D[LINE]
    B --> D[LINE]
    C --> D[LINE]
``` 

# Features
<!-- By specifying the ID on Google Drive, the photos will be overwritten. This ensures there is no worry about consuming too much storage space.

Google Drive上のidを指定することで写真を上書きします。容量を圧迫する心配がないです。 -->

# Requirement
* Python 3.12
* requests (chukyu.py)
* BeautifulSoup4 (jokyu.py)

# Installation
pipコマンドでrequests、BeautifulSoup4をインストールしてください。
Lambda関数として利用する場合はzipファイルとしてライブラリをインポートしてください

```bash
pip install requests # chukyu.py
pip install beautifulsoup4 # jokyu.py

pip install python-dotenv # Lambda以外で利用する場合
```

# Usage
リポジトリをクローンし、.envファイルを作成、トークンを記載しディレクトリ内にある任意のPythonコードを実行してください。


```bash
git clone https://github.com/daikidaiku/upload-lab-photo
cd upload-lab-photo
python3 main.py
``` 

.envファイル内は以下のように記載してください。
```bash
TOKEN='取得したアクセストークン'
```

# Note
LINE Notifyのトークン取得方法は以下の記事をご覧ください。

【Python】LINE Notifyの手引き #LineNotify - Qiita

<https://qiita.com/daikidaiku/items/4c364b393d4af16ac283>

# Author

* daiki_daiku
* Waseda University
* Twitter : https://twitter.com/daiki_da1ku

# License

lambda-line-notify is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).