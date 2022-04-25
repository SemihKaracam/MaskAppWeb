import requests
import json
import pymongo


myDatabase = pymongo.MongoClient("mongodb://localhost/maskapp") #maskapp adlı veritabanımıza bağlandık

users = myDatabase.maskapp.users # maskapp adlı veritabanımızın users adlı collection'ınını users adlı bir değişkene atadık.


# exist = users.find_one({"name":"Cem"})
# if(exist):
#     print(exist)
# else:
#     print("Kullanıcılar arasında bu isimde birisi yok")


url = "http://localhost:5000/posts"


fakeUsers = [{
    "name":"Cem",
    "email":"cem@gmail.com",
    "number":"2848887",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg"
},
{
    "name":"Semih",
    "email":"semih@gmail.com",
    "number":"1888887",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg"
},
{
    "name":"Mehmet",
    "email":"mehmet@gmail.com",
    "number":"1515515",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg"
},
{
    "name":"Barkin",
    "email":"barkin@gmail.com",
    "number":"2323235",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg"
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


# headers={
#     "content-type": "application/json"
# }
# i=0
# while(i<10):
#     if(i%2==0):
#         response = requests.post(url,data = json.dumps(data),headers=headers) # 2.parametrede data dictionary'mizi json formatına dönüştürüp backenda yolladık, 3.parametrede headers içerisine json yazarak requeste dönecek olan response'un veri formatının json olacağını bildirdik 
#         # print(response.text)
#     i+=1
