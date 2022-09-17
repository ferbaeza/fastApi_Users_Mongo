def taskEntity(item)->dict:
    return{
        'id': str(item['_id']),
        'title':item['title'],
        'author':item['author'],
        'body':item['body']
    }

def tasksEntity(entity)->list:
    return [taskEntity(item) for item in entity]