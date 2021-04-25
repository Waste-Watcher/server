import graphene
#from graphene import ObjectType, String, Schema, Int, List, Mutation, Field, ID, Boolean
from flask import Flask, request
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET KEY'] = ''

db = SQLAlchemy(app)
db.create_all()

class userData(db.Model):
    identification = db.Column(db.String(80), primary_key=True,unique=True)
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

class userInfo(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    earth_coins = graphene.Int(required = False)

class Query(graphene.ObjectType):
    getUser = graphene.String(id=graphene.String())
    def resolve_getUser(parent, id):
        return f"{userInfo.id}, {userInfo.name}"

class newUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        email = graphene.String()
    user = graphene.Field(lambda: userInfo)
    ok = graphene.Boolean()

    def mutate(id, name, email):
        user = userInfo(id = id, name = name, email = email, earth_coins = 0)
        sqlUser = userData(id = id, name = name, email = email, earth_coins = 0)
        db.session.add(sqlUser)
        db.session.commit()
        
        ok = True
        print(user)
        return newUser(user = user, ok = ok)

class Mutations(graphene.ObjectType):
    new_user = newUser.Field()

schema = graphene.Schema(query = Query, mutation = Mutations)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))

app.run()