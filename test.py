import json
import requests

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'


def get_resource1():
    respones=requests.get(BASE_URL+ENDPOINT)
    print(respones.status_code)
    print(respones.json())


def get_resource2(id):
    BASE_URL='http://127.0.0.1:8000/'
    ENDPOINT='api2/'

    respones=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(respones.status_code)
    print(respones.json())

def create_resource():

    stud_data={'name':'sachin','rollno':200,'marks':78,'address':'Mumbai'}
    respones=requests.post(BASE_URL+ENDPOINT,data=json.dumps(stud_data))
    print(respones.status_code)
    print(respones.json())

def update_resource(id):
    BASE_URL='http://127.0.0.1:8000/'
    ENDPOINT='api2/'

    stud_data={'name':'vismaya rao','marks':97}
    respones=requests.put(BASE_URL+ENDPOINT+id+'/',data=json.dumps(stud_data))
    print(respones.status_code)
    print(respones.json())

def delete_resource(id): 
    BASE_URL='http://127.0.0.1:8000/'
    ENDPOINT='api2/'

    respones=requests.delete(BASE_URL+ENDPOINT+id+'/')
    print(respones.status_code)
    print(respones.json())
print("...............................")
ch=int(input("Enter the value \n 1---> All record \n 2---> based on ID \n 3---> createnew record \n 4---> update_record \n 5---> To delete a record : "))
if ch==1:
    get_resource1()

elif ch==2:
    id=input("enter the id")
    get_resource2(id)

elif ch==3:
    create_resource()

elif ch==4:
    id=input("enter the id:")
    update_resource(id)
elif ch==5:
    id=input("Enter id")
    delete_resource(id)