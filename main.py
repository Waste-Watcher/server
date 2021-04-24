from graphene import ObjectType, String, Schema
from flask import Flask, request

class Query(objectType):
    user = String(
    id = String()
    email = String()
    points = String()
    )

    def resolve_user(root, info, id):
        return 
schema = Schema(query=Query)

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def main():
    if request.method == "POST":
        pass
    if request.method == "GET":
        pass
    return 

app.run()
