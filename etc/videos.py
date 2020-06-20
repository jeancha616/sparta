import json
import requests
import comment

url = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyC2m2Jh9ddGZhMcg8L3JwhZ6qiSHg9gr7k&channelId=UC8HNshpReWjQv1WpwzhPHjA&part=snippet&maxResults=1&order=date'
data = requests.get(url)
json_data = json.loads(data.text)  # json 데이터를 파싱
print (json_data)
for i in json_data['items']:
    if i['id']:
        if 'videoId' in i['id'].keys():
            print(i)
            print ('https://www.youtube.com/watch?v=' + i['id']['videoId'][])
            # print (comment.commentExtract(i['id']['videoId']))