from fastapi import FastAPI
from routes.user import user
from routes.task import task

app = FastAPI()

app.include_router(user)
app.include_router(task)


@app.get('/')
def index():
    return {'Message':'This is a FastApi backend'}

