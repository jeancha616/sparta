from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://cyjid:cyjpw@localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

import json
import requests
import comment
import time

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/monitor', methods=['GET'])
def listing():
    # 1. 모든 모니터정보 찾기 / 이 때 모니터정보가 불려오는 곳은 db.monitors 
    all_monitors = list(db.monitors.find({},{"_id":0}))
    
    # 2. monitors라는 키값으로 모니터정보를 내려준다
    return jsonify({'result':'success', 'monitors' : all_monitors})

@app.route('/monitor', methods=['POST'])
def monitoring():
    # 클라이언트로부터 받아온 url에서 동영상의 코드를 뽑아낸다
    url = request.form['url_give']

    split_url = url.split('?v=')
    url_edit = split_url[-1]

    api = "https://www.googleapis.com/youtube/v3/videos?key=AIzaSyC2m2Jh9ddGZhMcg8L3JwhZ6qiSHg9gr7k&id={0}&part=snippet".format(url_edit)
    data = requests.get(api)
    json_data = json.loads(data.text)  # json_data 를 파싱
    
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    thumbnail = json_data['items'][0]['snippet']['thumbnails']['high']['url']
    title = json_data['items'][0]['snippet']['title']
    date = json_data['items'][0]['snippet']['publishedAt']

    # python 문자열 치환 
    date = date.replace("T", " ").replace("Z", "")
    comment_list = comment.commentExtract(url_edit)

    # mongoDB에 데이터 넣기
    doc = {  
            'now' : now,
            'url' : url, 
            'thumbnail' : thumbnail,
            'title' : title, 
            'date' : date,
            'comment' : comment_list
            }

    # monitors라는 이름으로 DB를 저장한다
    db.monitors.insert_one(doc)
    # 성공하면, 메시지를 띄웁니다 
    return jsonify({'result' : 'success', 'msg' : 'Monitor Completed'})

@app.route('/monitor/delete', methods=['POST'])
def delete_monitoring():
    # 클라이언트로부터 받아온 now_give를 now_receive 변수에 넣습니다
    now_receive = request.form['now_give']
    print(now_receive)
    # monitors 목록에서 delete_one으로 now가 now_receive와 일치하는 항목을 제거합니다
    db.monitors.delete_one({'now': now_receive})
    # 성공하면, 메시지를 띄웁니다
    return jsonify({'result' : 'success', 'msg':'삭제되었습니다'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
