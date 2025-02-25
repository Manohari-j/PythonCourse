try:
    import graphene
    import json
    import os

    print("All ok")
except Exception as e:
    print("Error : {}".format(e))

DATA = [
    {
    "name": "Mano",
    "age": "39"
    },
    {
        "name": "Jai",
        "age": "42"
    }
]


# resolve and name of the argument that we are resolving

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()


class Query(graphene.ObjectType):
    array = graphene.List(Person, size=graphene.Int(default_value=1))

    def resolve_array(root, info, size):
        return DATA[:size]

schema = graphene.Schema(query=Query)
# print(schema)

# Graph QL Query
query_graph = '''
query myquery{
     array(size:2){
        name
        age
     }
}
'''
result = schema.execute(query_graph)
# print(result.data)
print(json.dumps(result.data, indent=3))
