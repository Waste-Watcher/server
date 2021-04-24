from graphene import ObjectType, String, Schema, Int, List, Mutation, Field, ID, Boolean
from flask import Flask, request
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET KEY'] = ''
db = SQLAlchemy(app)

class userData(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #avatar = db.Column(db.String(120),nullable=False,default = default.jpg)
    earth_coins = db.Column(db.Integer(), nullable = False)
    def __repr__(self):
        return f"{self.name},{self.email},{self.earth_coins}"
    def update_earth_coins(self,newamount):
        self.earth_coins = newamount
    #def update_avatar(self,newavatar):
    #   self.newavatar = newavatar
    
class Item(db.Model):
    itemid = db.Column(db.String(80), primary_key=True)
    ownerid = db.Column(db.String(80), nullable=False)
    item_type = db.Column(db.String(120), nullable=False)
    def __repr__(self):
        return f"{self.item_type},{self.ownerid}"
'''
@app.route("/", methods = ["GET","POST"])
def getGraphQL():
    return(request.data)
'''
app.run()

class User(ObjectType):
    id = ID()
    name = String()
    email = String()
    earth_coins = Int()

class Query(ObjectType):    
    def resolve_User(self, info, id):
        return User()

class newUser(Mutation):
    class Arguments:
        id = String()
        name = String()
        email = String()
        earth_coins = Int()

    ok = Boolean()

    user = Field(User)

    def mutate(self, info, id, name, earth_coins):
        user = User(id = id, name = name, email = email, earth_coins = earth_coins)
        sqlUser = userData(id = id, name = name, email = email, earth_coins = earth_coins)
        db.session.add(sqlUser)
        db.session.commit()
        ok = True
        print(user)
        return newUser(user = user, ok = ok)

class Mutations(ObjectType):
    new_user = newUser.Field()

schema = Schema(query=Query, mutation = Mutations)

def add_user(id, name, earth_coins):
    new = schema.execute(
        """
            mutation newUser($id: String) {
                newUser(id: $id, name: "test", earth_coins: 4){
                    user {
                        id
                        name
                        earth_coins
                    }
                    
                }        
            }
        """,variable_values={"id" : id, "name" : name, "earth_coins" : earth_coins}
    )
    return new

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))