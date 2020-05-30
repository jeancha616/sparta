from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##

movie = db.movies.find_one({'title':'매트릭스'})
matrix_star = movie['star']
# print(movie['star'])

matrix_list = list(db.movies.find({'star':matrix_star}))
#star가 matrix_star와 같은 것을 찾아서 리스트에 넣어주고, 그 리스트의 이름을 matrix_list라고 한다

for ml in matrix_list:
    db.movies.update_one({'title':ml['title']}, {'$set':{'star':0}})

    print(ml['title']) #제목의 키는 'title'이니까, 
    #키값을 가져올 때, [ ] 

