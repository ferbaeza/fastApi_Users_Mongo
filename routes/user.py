from fastapi import APIRouter
from schema.user import userEntity, usersEntity
from config.database import collection_name
from models.userModel import User
from bson import ObjectId

user= APIRouter()


@user.get('/users')
async def get_all_users():
    users = usersEntity(collection_name.find())
    return {'Message': 'Users Done', 'data': users}
    #return{'data': 'Get all Users'}

@user.get('/users/{id}')
async def get_user(id:str):
    user = userEntity(collection_name.find({'_id':ObjectId(id)}))
    return {'Message': 'Single User Done', 'data': user}

@user.post('/users')
async def create_new_user(user:User):
    _id= collection_name.insert_one(dict(user))
    newuser = userEntity(collection_name.find({'_id':_id.inserted_id}))
    return {'Message': 'New User Done', 'data': newuser}

    return{'data': 'Create a new User'}


@user.put('/users/{id}')
def modify_user():
    return{'data': 'Modify User'}

@user.delete('/users/{id}')
def delete_user():
    return{'data': 'Delete User'}

