# req.py - autotest for the app

import requests
import json
print(dir(requests))
response = requests.get("http://jsonplaceholder.typicode.com/comments")
print( response.status_code)
print( response.content)
comments = json.loads(response.content)
comments = json.loads(response.content)
print( comments[0])
print( comments[0]['body'])
for comment in comments[0:10]:
    print( comment['name'])
response = requests.get("http://jsonplaceholder.typicode.com/comments/1")
print(response.content)

post = requests.get("http://jsonplaceholder.typicode.com/posts/%d" % comment['postId'])
print(post.content)
post = json.loads(post.content)
print(post)
print(post['title'])
dados = data={"postId": 1, "name": "John Doe", "email": "john@doe.com", "body": "This is it!"}
response = requests.post("http://jsonplaceholder.typicode.com/comments/", data=dados)
print(response.status_code)
print( response.content)
dados = {"email": "john@doe.com"}
response = requests.put("http://jsonplaceholder.typicode.com/comments/10", data=dados)

response = requests.delete("http://jsonplaceholder.typicode.com/comments/10")

response = requests.get("http://jsonplaceholder.typicode.com/posts/2/comments")

