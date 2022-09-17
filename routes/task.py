from fastapi import APIRouter
from schema.task import taskEntity, tasksEntity
from config.database import collection_tasks
from models.taskModel import Task
from bson import ObjectId

task= APIRouter()


@task.get('/tasks')
async def get_all_tasks():
    tasks = tasksEntity(collection_tasks.find())
    return {'Message': 'Tasks Done', 'data': tasks}
    #return{'data': 'Get all Tasks'}

# @task.get('/users/{id}')
# async def get_user(id:str):
#     user = userEntity(collection_name.find_one({'_id':ObjectId(id)}))
#     return {'Message': 'Single User Done', 'data': user}

@task.post('/tasks')
async def create_new_task(task:Task):
    _id= collection_tasks.insert_one(dict(task))
    newtask = taskEntity(collection_tasks.find_one({'_id':_id.inserted_id}))
    return {'Message': 'New User Done', 'data': newtask}

    return{'data': 'Create a new User'}


# @task.put('/users/{id}')
# async def modify_user(id:str, user:User):
#     userEntity(collection_name.find_one_and_update({'_id':ObjectId(id)},{
#         '$set':dict(user)
#     }))
#     return{'message':'User updated','data': {'User_id':id,'data_mod':user}}

# @task.delete('/users/{id}')
# async def delete_user(id:str):
#     user= userEntity(collection_name.find_one_and_delete({'_id':ObjectId(id)}))
#     return{'message': 'Usewr deleted','data': []}

