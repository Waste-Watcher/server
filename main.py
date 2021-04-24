from graphene import ObjectType, String, Schema
from flask import Flask, request

class Query(objectType):
    pass

app = Flask(__name__)

@app.route("/")
def main():
    pass

app.run()
