from graphene import ObjectType, String, Schema, Mutation, ID, Int

class Query(ObjectType):
    hello = String(name=String(default_value="名無しさん"))

    def resolve_hello(self, info, name):
        return f'こんにちは {name}さん'

class CreatePerson(Mutation):

    create_id = ID()
    create_name = String()
    create_age = Int()

    class Arguments:
        name = String()
        age = Int()

    def mutate(self, info, name, age):
        return CreatePerson(
            create_id=1,
            create_name =f'{name}さん',
            create_age =age+10,
        )

class MyMutation(ObjectType):
    create_person = CreatePerson.Field()

schema = Schema(query=Query, mutation=MyMutation)