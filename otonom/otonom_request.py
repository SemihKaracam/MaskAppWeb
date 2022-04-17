import requests
import json
url = "http://localhost:5000/posts"

data={
    "name":"Cem",
    "email":"cem@gmail.com",
    "number":"2848887",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg"
}


headers={
    "content-type": "application/json"
}
i=0
while(i<10):
    if(i%2==0):
        response = requests.post(url,data = json.dumps(data),headers=headers) # 2.parametrede data dictionary'mizi json formatına dönüştürüp backenda yolladık, 3.parametrede headers içerisine json yazarak requeste dönecek olan response'un veri formatının json olacağını bildirdik 
        print(response.text)
    i+=1
