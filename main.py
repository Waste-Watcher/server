from graphene import ObjectType, String, Schema, Int, List, Mutation, Field, Boolean
from flask import Flask, request

class User(ObjectType):
    id = String()
    name = String()
    coinCount = Int()

class Query(ObjectType):
    userList = List(User)
    
    def resolve_userList(self, info, id):
        return [
            User(id="1234",name="asa",coinCount=10),
            User(id="5678",name="bob",coinCount=12)
        ]

class newUser(Mutation):
    class Arguments:
        print(1)
        id = String()
        name = String()
        coinCount = Int()
        print(2)

    ok = Boolean()

    tempUser = Field(User)
    print(3)
    def mutate(self, info, id, name, coinCount):
        print(4)
        tempUser = User(id = id, name = name, coinCount = coinCount)
        ok = True
        print(tempUser)
        return newUser(tempUser = tempUser, ok=ok)

class Mutations(ObjectType):
    new_user = newUser.Field()

schema = Schema(query=Query, mutation = Mutations)

answ = schema.execute(
    """
        mutation newUser {
            newUser(id: "12345", name: "test", coinCount: 4){
                id
                name
                coinCount
            }        
        }
    """
) 
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