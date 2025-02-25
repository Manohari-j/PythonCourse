import json

import graphene
from graphene import Field, String, List

from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query
from type import User


class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


class MyQuery(Query):
    user = graphene.Field(User)
    get_user = Field(User, id=String())
    get_users = graphene.List(User)


schema = graphene.Schema(query=MyQuery, mutation=MyMutations)
# print(schema)
# mutation_graph = '''
# mutation {
#     createUser(id:"1",name:"Mano",email:"mano@gmail.com",password:"123456")
#         {
#             user{
#                 id
#                 name
#                 email
#                 password
#             }
#         }
# }
# '''

# mutation_graph = '''
# mutation {
#     updateUser(id:"1",name:"Jai",email:"jai@gmail.com",password:"99999")
#         {
#             user{
#                 id
#                 name
#                 email
#                 password
#             }
#         }
# }
# '''
# mutation_graph = '''
# mutation {
#     deleteUser(id:"1")
#         {
#             user{
#                 id
#                 name
#                 email
#                 password
#             }
#         }
# }
# '''

mutation_graph = '''
query {
    getUser(id:"1")
        {
            id
            name
            email
            password

        }
}
'''

# mutation_graph = '''
# query {
#     getUsers{
#         id
#         name
#         email
#         password
#     }
# }
# '''
result = schema.execute(mutation_graph)
print(json.dumps(result.data,indent = 3))

