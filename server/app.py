# from crypt import methods
from flask import Flask, request,jsonify
from flask_pymongo import PyMongo,ObjectId
from flask_cors import CORS
from pymongo import MongoClient


# app = Flask(__name__)
# cors = CORS(app)
# app.config["MONGO_URI"] = "mongodb+srv://semih:semih@cluster0.ceuft.mongodb.net/?retryWrites=true&w=majority"
# mongo = PyMongo(app)
# db = mongo.db.users


app = Flask(__name__)
try:
    client = MongoClient("mongodb+srv://semih:semih123@cluster0.ceuft.mongodb.net/?retryWrites=true&w=majority")
    db = client["test"]
    collection = db["users"]
    print("Baglanti kuruldu")
except Exception as e:
    print(e)
# collection.insert_one({"name":"Kerem","number":"12345"})
# print("Veri basariyla eklendi")


@app.route("/",methods=["GET"])
def getUsers():
    users = list(collection.find({}))   
    for user in users:
        user["_id"] = str(user["_id"])
    return jsonify({"res":users})

@app.route("/users",methods=["POST"])
def createUser():
    user = request.json
    id = collection.insert_one(user).inserted_id
    user["_id"] = str(id)
    return jsonify({"user":user,"msg":"user added"})

@app.route("/users/<id>",methods=["PUT"])
def updateUser(id):
    user = collection.find_one({"_id":ObjectId(id)})
    user["cezapuani"] = int(user["cezapuani"]) + 10
    collection.update_one({"_id":ObjectId(id)},{"$set":user})
    user["_id"] = str(id)
    return jsonify({"user":user,"msg":"user updated"})

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/",methods=["GET"])
# def getUsers():
#     users = list(db.find({}))
#     for user in users:
#         user["_id"] = str(user["_id"])
#     return jsonify({"res":users})

# @app.route("/posts",methods=["POST"])
# def createUser():
#     user = {"name":request.json["name"],
#             "email":request.json["email"],
#             "cezapuani":"10",
#             "number":request.json["number"],
#             "image":request.json["image"],
#             }
#     id = db.insert_one(user).inserted_id
#     user["_id"] = str(id)
#     return jsonify({"user":user,"msg":"user added"})


# @app.route("/posts/<id>",methods=["PUT"])
# def updateUser(id):
#     user = db.find_one({"_id":ObjectId(id)})
#     cezapuani = str(int(user["cezapuani"]) + 10)
#     db.update_one({"_id":ObjectId(id)},{"$set":{
#         "name":user["name"],
#         "email":user["email"],
#         "cezapuani":cezapuani,
#         "number":user["number"],
#         "image":user["image"],
#     }})
#     return jsonify({"msg":"User updated"})

# @app.route("/posts/<id>",methods=["DELETE"])
# def deleteUser(id):
#     db.delete_one({"_id":ObjectId(id)})
#     return jsonify({"msg":"User deleted"})


# if __name__ == "__main__":
#     app.run(debug=True)