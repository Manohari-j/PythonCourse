import uvicorn
from fastapi import FastAPI


def init_app():
    apps = FastAPI(
        title="My Python GraphQL",
        description="Fast API",
        version="1.0.0"
    )

    # simple endpoint
    @apps.get('/')
    def home():
        return "Welcome Home!"

    return apps

app=init_app()

if __name__ == '__main__':
    uvicorn.run("mainapi:app",host="localhost", port=8888,reload=True)

