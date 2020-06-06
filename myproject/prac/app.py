from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
# jsonify: 제이슨으로 만들어준다 request: 변수를 받아온다 (requests 와 request는 다름)
# flask 에서 남들이 미리 개발해놓은 친구들을 가져와서 쓴다

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분 #api는 '/test' 
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   name_receive = request.form['name_give'] #name_give로 보내주었으니, 여기서 name_receive로 받는다 
   print(title_receive, name_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   name_receive = request.args.get['name_give']
   print(title_receive, name_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
   # jsonify를 통해 글자를 json형식으로 만들어 주었답니다

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

