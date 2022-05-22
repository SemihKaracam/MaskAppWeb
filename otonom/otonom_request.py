import requests
import json
import pymongo


myDatabase = pymongo.MongoClient("mongodb+srv://semih:semih123@cluster0.ceuft.mongodb.net/?retryWrites=true&w=majority") #maskapp adlı veritabanımıza bağlandık

users = myDatabase.test.users # maskapp adlı veritabanımızın users adlı collection'ınını users adlı bir değişkene atadık.


url = "http://localhost:5000/users"


fakeUsers = [{
    "name":"Cem",
    "email":"cem@gmail.com",
    "number":"2848887",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg",
    "cezapuani":0
},
{
    "name":"Semih",
    "email":"semih@gmail.com",
    "number":"1888887",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg",
    "cezapuani":0
},
{
    "name":"Mehmet",
    "email":"mehmet@gmail.com",
    "number":"1515515",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg",
    "cezapuani":0
},
{
    "name":"Barkin",
    "email":"barkin@gmail.com",
    "number":"2323235",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg",
    "cezapuani":0
},

]


headers={
    "content-type": "application/json"
}

for u in fakeUsers:
    user = users.find_one({"email":u["email"]})
    
    if(user):
        requests.put(f"{url}/{str(user['_id'])}",headers=headers)
    else:
        requests.post(url,data=json.dumps(u),headers=headers)

    

data={
    "name":"Cem",
    "email":"cem@gmail.com",
    "number":"2848887",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg"
}

