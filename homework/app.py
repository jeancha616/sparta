from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def order(): 
    #1 클라이언트가 준 주문자 이름/수량/주소/전화번호 가져오기
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    adress_receive = request.form['adress_give']
    contact_receive = request.form['contact_give']

    #2 DB에 정보 삽입하기 
    doc = {
        'name': name_receive,
        'quantity': quantity_receive,
        'adress': adress_receive,
        'contact': contact_receive 
    }  
    db.order.insert_one(doc)

    #3 성공여부 & 성공메세지 반환하기 
    return jsonify({'result':'success', 'msg': '주문이 완료되었습니다'})

@app.route('/orders', methods=['GET'])
def show_orders():
    #1 DB에서 주문 정보 모두 가져오기
    #_id는 가져오지 않을 거에요
    orders = list(db.order.find({}, {'_id':False})) 
    #2 성공여부 & 리뷰목록 반환하기
    #'all_order'라는 키로 orders를 꺼내 올 것입니다
    return jsonify({'result':'success', 'all_order': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)