import requests
import json
url = 'http://127.0.0.1:8000/student/'


def get_student(id=None):
    data={}
    if id is not None:
        data={'id':id}
    jason_data = json.dumps(data)
    r = requests.get(url=url, data=jason_data)
    res = r.json()
    print(res)
 
# get_student()

def create_data():
    data={
        'name':'bezos',
        'gender':'Male',
        'country':'USA',
        'age':55
    }
    
    jason_data = json.dumps(data)
    r = requests.post(url=url, data=jason_data)
    res = r.json()
    print(res)

create_data()

def update_data():
    data={
        'id':3,
        'name':'Bndrew Tate',
        'age':30
    }
    
    jason_data = json.dumps(data)
    r = requests.put(url=url, data=jason_data)
    res = r.json()
    print(res)
# update_data()