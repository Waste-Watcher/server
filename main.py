from graphene import ObjectType, String, Schema, Int, List, Mutation, Field, Boolean
from flask import Flask, request

class User(ObjectType):
    id = String()
    name = String()
    coinCount = Int()

class Query(ObjectType):
    userList = List(User)
    
    def resolve_userList(self, info, id):
        return self.userList

class newUser(Mutation):
    class Arguments:
        id = String()
        name = String()
        coinCount = Int()

    ok = Boolean()

    user = Field(User)

    def mutate(self, info, id, name, coinCount):
        user = User(id = id, name = name, coinCount = coinCount)
        ok = True
        print(user)
        return newUser(user = user, ok = ok)

class Mutations(ObjectType):
    new_user = newUser.Field()

schema = Schema(query=Query, mutation = Mutations)

answ = schema.execute(
    """
        mutation newUser($id: String) {
            newUser(id: $id, name: "test", coinCount: 4){
                user {
                    id
                    name
                    coinCount
                }
                
            }        
        }
    """,variable_values={"id" : "12345", "name" : "test", "coinCount" : "4"}
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