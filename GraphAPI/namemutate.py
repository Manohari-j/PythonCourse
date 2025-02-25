try:
    import graphene
    import json
    import os

    print("All ok")
except Exception as e:
    print("Error : {}".format(e))


# resolve and name of the argument that we are resolving

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()


# Mutate

class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(Person)

    def mutate(self, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)


class MyMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()  # _ will be converted to camel case


class Query(graphene.ObjectType):
    person = graphene.Field(Person)


schema = graphene.Schema(query=Query, mutation=MyMutation)
print(schema)

# Graph QL Query with mutation
query_graph = '''
mutation myFirstMutation{
     createPerson(name:"Manohari"){
        person{
            name
            
        }
        ok
     }
}
'''
result = schema.execute(query_graph)
# print(result.data)
print(json.dumps(result.data, indent=3))
