

from flask import Flask, request,jsonify
from flask_pymongo import PyMongo,ObjectId
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost/maskapp"
mongo = PyMongo(app)

db = mongo.db.users

##########################################################
#OTONOM İSTEK KISMI
# import requests
# import json
# url = "http://localhost:5000/posts"

# payload={
#     "name":"Cem",
#     "email":"cem@gmail.com",
#     "number":"2848887",
#     "image":"https://m.media-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg"
# }

# i=0
# while(i<10):
#     if(i%2==0):
#         response = requests.post(url,data = json.dumps(payload))
#         print(response)
#     i+=1
####################################################

@app.route("/",methods=["GET"])
def getUsers():
    users = list(db.find({}))
    for user in users:
        user["_id"] = str(user["_id"])
    return jsonify({"res":users})

@app.route("/posts",methods=["POST"])
def createUser():
    user = {"name":request.json["name"],
            "email":request.json["email"],
            "cezapuani":"10",
            "number":request.json["number"],
            "image":request.json["image"],
            }
    id = db.insert_one(user).inserted_id
    user["_id"] = str(id)
    return jsonify({"user":user,"msg":"user added"})


@app.route("/posts/<id>",methods=["PUT"])
def updateUser(id):
    user = {"name":request.json["name"],
            "email":request.json["email"],
            "cezapuani":request.json["cezapuani"],
            "number":request.json["number"],
            "image":request.json["image"],
            }
    user = db.find_one({"_id":ObjectId(id)})
    cezapuani = str(int(user["cezapuani"]) + 10)
    db.update_one({"_id":ObjectId(id)},{"$set":{
        "name":user["name"],
        "email":user["email"],
        "cezapuani":cezapuani,
        "number":user["number"],
        "image":user["image"],
    }})
    return jsonify({"msg":"User updated"})

@app.route("/posts/<id>",methods=["DELETE"])
def deleteUser(id):
    db.delete_one({"_id":ObjectId(id)})
    return jsonify({"msg":"User deleted"})
if __name__ == "__main__":
    app.run(debug=True)