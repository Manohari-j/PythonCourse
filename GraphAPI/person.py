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


class PersonInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    age = graphene.String(required=True)


# Mutate

class CreatePerson(graphene.Mutation):
    class Arguments:
        person_data = PersonInput(required=True)

    person = graphene.Field(Person)

    def mutate(root, info, person_data):
        person = Person(name=person_data.name, age=person_data.age)
        return CreatePerson(person=person)


class MyMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()  # _ will be converted to camel case


class Query(graphene.ObjectType):
    person = graphene.Field(Person)


schema = graphene.Schema(query=Query, mutation=MyMutation)
print(schema)

# Graph QL Query with mutation
query_graph = '''
mutation myFirstMutation{
     createPerson(personData:{name:"Manohari",age:"39"}){
        person{
            age
            name

        }
        
     }
}
'''
result = schema.execute(query_graph)
# print(result.data)
print(json.dumps(result.data, indent=3))
