
from fastapi import APIRouter,HTTPException,status
from . import userschema
from random import randrange

router= APIRouter(tags=["USER Application"])

# dummy user data

usersData=[{'uname':'Sam','email':'sam@mail.com','city':'NY','id':101}]

# search common logic

def searchUser(id):
    for index,data in enumerate(usersData):
        if(data['id'] == id):
            return index
# load the data from server
@router.get('/users/loadusers')
def welcomeUser():
    return {'message':usersData}

# add the data from server
@router.post('/users/adduser')
def adduser(payload: userschema.Users):
    userdata= payload.model_dump()
    userdata['id']=randrange(0,1000)
    usersData.append(userdata)
    return {'message':userdata}

# search the data from server
@router.get("/users/finduser/{id}")
def findUser(id:int):
    serachResult= searchUser(id)
    if serachResult== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='OOPS,.... user not found with matching ID')
    return{"result":serachResult}


# remove the data from server
@router.delete("/users/deleteuser/{id}")
def deleteUser(id:int):
    serachResult= searchUser(id)
    if serachResult== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='OOPS,.... user not found with matching ID')
    usersData.pop(serachResult)
    return{"result":'user deleted'}

# update the data from server
@router.put("/users/updateuser/{id}")
def updateUser(id:int,payload: userschema.Users):
    serachResult= searchUser(id)
    if serachResult== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='OOPS,.... user not found with matching ID')
    
    myuser=payload.model_dump()
    myuser['id']=id
    usersData[serachResult]=myuser

    return{"result":'user updated'}


