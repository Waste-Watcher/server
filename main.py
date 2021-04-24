from graphene import ObjectType, String, Schema, Int, List
from flask import Flask, request

class user(ObjectType):
    id = String()
    name = String()
    coinCount = Int()

class Query(ObjectType):
    userList = List(user)
    
    def resolve_userList(self, info):
        return [
            user(id="1234",name="asa",coinCount=10),
            user(id="5678",name="bob",coinCount=12)
        ]

schema = Schema(query=Query)

answ = schema.execute("""
{
    userList {
        id
        name
    }
}
""") 
print(answ)
'''
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def main():
    if request.method == "POST":
        pass
    if request.method == "GET":
        pass
    return 

app.run()
'''