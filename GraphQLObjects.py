import graphene
from database import User, db

class userInfo(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    earth_coins = graphene.Int(required = False)

class Query(graphene.ObjectType):
    getUser = graphene.String(id=graphene.String())
    def resolve_getUser(root, id):
        user = User.query.filter_by(id = id).first()
        if not user:
            return
        return userInfo(id = user.id, name = user.name, email = user.email, earth_coins = user.earth_coins)


class newUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        email = graphene.String()
    user = graphene.Field(lambda: userInfo)
    ok = graphene.Boolean()

    def mutate(root, info, id, name, email):
        print(1) # this does not get printed
        user = userInfo(id = id, name = name, email = email, earth_coins = 0)
        sqlUser = User(identification = id, name = name, email = email, earth_coins = 0)
        db.session.add(sqlUser)
        db.session.commit()

        ok = True
        print(user)
        return newUser(user = user, ok = ok)

class Mutations(graphene.ObjectType):
    new_user = newUser.Field()
