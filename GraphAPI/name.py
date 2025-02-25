try:
    import graphene
    import json
    import os
    print("All ok")
except Exception as e:
    print("Error : {}".format(e))

"""
 {
    name:"Mano",
    age: 39
 }    
 """
# resolve and name of the argument that we are resolving


class Query(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()

    def resolve_name(root, info):
        return "Mano"

    def resolve_age(root, info):
        return "39"


schema = graphene.Schema(query=Query)
# print(schema)

# Graph QL Query
query_graph = '''
query myquery{
     N:name
     A:age
}
'''
result = schema.execute(query_graph)
print(result.data)
