from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

import json
import requests
import comment

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/monitor', methods=['GET'])
def listing():
    # 1. 모든 모니터정보 찾기 / 이 때 모니터정보가 불려오는 곳은 db.monitors 
    all_monitors = list(db.monitors.find({}))
    
    # 2. monitors라는 키값으로 모니터정보를 내려준다
    return jsonify({'result':'success', 'monitors' : all_monitors})

## API 역할을 하는 부분
## API: 원래 하고 싶었던 것은, 입력한 url에서 정보를 끌어오는 것
## API: 현재는 YouTube 채널에서 가장 최근 N개 게시물의 정보를 불러옴
@app.route('/monitor', methods=['POST'])
def monitoring():
    api = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyC2m2Jh9ddGZhMcg8L3JwhZ6qiSHg9gr7k&channelId=UC8HNshpReWjQv1WpwzhPHjA&part=snippet&maxResults=1&order=date'
    data = requests.get(api)
    json_data = json.loads(data.text)  # json_data 를 파싱
    # print (json_data)
    for i in json_data['items']:
        if i['id']:
            if 'videoId' in i['id'].keys():

                thumbnail = i['snippet']['thumbnails']['default']['url']
                title = i['snippet']['title']
                date = i['snippet']['publishedAt']
                comment = comment.commentExtract(i['id']['videoId'])

    ## mongoDB에 데이터 넣기
    doc = {
            'thumbnail' : thumbnail,
            'title' : title, 
            'date' : date,
            'comment' : comment
    }

    ## monitors라는 이름으로 DB를 저장한다
    db.monitors.insert_one(doc)

    return jsonify({'result' : 'success', 'msg' : '저장이 완료되었습니다'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
