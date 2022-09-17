######  FerBaeza

## FastApi backend *MongoDB_Atlas*
# First Steps
* [Installation](#installation)
* [Scaffold](#scaffold)


## Installation
```bash
$ mkdir project_name
$ cd project_name
$ python3 -m virtualenv venv
$ source venv/bin/activate
(venv)$ pip install fastapi uvicorn pymongo pymongo[srv]
uvicorn main:app --reload
```


## Scaffold
* project_folder
    * config
    * models
    * routes
    * schema