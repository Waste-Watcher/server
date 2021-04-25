import graphene
from database import User, Item, db

class itemInfo(graphene.ObjectType):
    id = graphene.String()
    owner_id = graphene.String()
    item_name = graphene.String()

class userInfo(graphene.ObjectType):
    id = graphene.String()
    display_name = graphene.String()
    email = graphene.String()
    earth_coins = graphene.Int()
    items = graphene.List(itemInfo)

class Query(graphene.ObjectType):
    User = graphene.Field(userInfo, id=graphene.String())

    def resolve_User(root, parent, id):
        user = User.query.filter_by(id = id).first()
        if user is not None:
            items_query = Item.query.filter_by(owner_id=id).all()
            if items_query is not None:
                items = [itemInfo(id=item.id, owner_id=item.owner_id, item_name=item.item_name) for item in items_query]
            else:
                items = []
            return userInfo(
                id=user.id,
                display_name=user.display_name,
                email=user.email,
                earth_coins=user.earth_coins,
                items=items
            )
        else:
            return {}
    
    def resolve_Item(root, parent, id):
        item = Item.query.filter_by(id=id).first()
        if item is not None:
            return itemInfo(
                id=item.id,
                owner_id=item.owner_id,
                item_name=item.item_name
            )

class newUser(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        display_name = graphene.String()
        email = graphene.String()
    user = graphene.Field(lambda: userInfo)
    ok = graphene.Boolean()

    def mutate(root, info, id, display_name, email):
        print(1) # this does not get printed
        user = userInfo(id = id, display_name = display_name, email = email, earth_coins = 0, items=[])
        sqlUser = User(id = id, display_name = display_name, email = email, earth_coins = 0)
        db.session.add(sqlUser)
        db.session.commit()

        ok = True
        print(user)
        return newUser(user = user, ok = ok)

class newItem(graphene.Mutation):
    class Arguments:
        owner_id = graphene.String()
        item_name = graphene.String()

    item = graphene.Field(lambda: itemInfo)
    ok = graphene.Boolean()

    def mutate(self, info, owner_id, item_name):
        sqlItem = Item(owner_id=owner_id, item_name=item_name)
        db.session.add(sqlItem)
        db.session.flush()
        item = itemInfo(id=sqlItem.id, owner_id=owner_id, item_name=item_name)
        db.session.commit()
        
        ok = True
        print(item)
        return newItem(item=item, ok=ok)


class Mutations(graphene.ObjectType):
    new_user = newUser.Field()
    new_item = newItem.Field()
