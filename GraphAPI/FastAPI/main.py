# 1. pip install fastapi pymysql sqlalchemy
# 2. pymysql - sql driver.  a lightweight and pure Python-based MySQL client library
# 3. Sqlalchemy : QLAlchemy is basically referred to as the toolkit of Python SQL
# 4. pip install 'strawberry-graphql[fastapi]' : create GraphQL endpoints in Python applications
# 5. pip install 'uvicorn[standard]' : Uvicorn is an ASGI web server implementation for Python.
# Uvicorn is a web server. It handles network communication - receiving requests from client applications such as users'
# browsers and sending responses to them
# 6. FastAPI is designed for rapid development and aims to maximize developer productivity through features
# like automatic validation, documentation, and type inference.
# pip install cryptography


from fastapi import FastAPI
from controllers.index import user
app = FastAPI()
app.include_router(user)
