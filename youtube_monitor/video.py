import json
import requests
import comment

url = "https://www.googleapis.com/youtube/v3/videos?key=AIzaSyC2m2Jh9ddGZhMcg8L3JwhZ6qiSHg9gr7k&id=gaGsZD42PhM&part=snippet"
data = requests.get(url)
json_data = json.loads(data.text)  # json_data 를 파싱

thumbnail = json_data['items'][0]['snippet']['thumbnails']['high']['url']
title = json_data['items'][0]['snippet']['title']
date = json_data['items'][0]['snippet']['publishedAt']

print(thumbnail)
print(title)
print(date)

# url = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyC2m2Jh9ddGZhMcg8L3JwhZ6qiSHg9gr7k&channelId=UC8HNshpReWjQv1WpwzhPHjA&part=snippet&maxResults=1&order=date'
# data = requests.get(url)
# json_data = json.loads(data.text)  # json_data 를 파싱
# # print (json_data)
# for i in json_data['items']:
#     if i['id']:
#         if 'videoId' in i['id'].keys():

#             thumbnail = i['snippet']['thumbnails']['default']['url']
#             title = i['snippet']['title']
#             date = i['snippet']['publishedAt']
#             link = 'https://www.youtube.com/watch?v=' + i['id']['videoId']
#             comment = comment.commentExtract(i['id']['videoId'])

#             print(thumbnail)
#             print(title)
#             print(date)
#             print(comment)


    