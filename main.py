import graphene
# from flask import Flask, request
from flask_graphql import GraphQLView
from dbinfo import app, db
from GraphQLObjects import Query, Mutations

schema = graphene.Schema(query = Query, mutation = Mutations)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))

@app.route('/', methods=["POST"])
def upload_image():
    data = request.get_json()
    base64 = data['data']
    print(base64)
    # TODO: Implement some machine learning stuff and see if the image met criteria
    return { "status": "successful" }

db.create_all()
app.run()