from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

import json
import requests
import comment
import video

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
## API: 원래 하고 싶었던 것은, 입력한 url에서 정보를 끌어오는 것
## API: 현재는 YouTube 채널에서 가장 최근 1개 게시물의 정보를 불러옴
