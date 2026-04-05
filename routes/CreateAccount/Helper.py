import hashlib
import base64
import uuid
from models.LoginSql import db,User
from sqlalchemy.exc import IntegrityError


# class User(db.Model):
#     __tablename__="User"
#     id = db.Column(db.Integer, primary_key=True,unique=True,autoincrement=True)
#     Username=db.Column(db.String(50),nullable=False,unique=True)
#     Password=db.Column(db.String(256),nullable=False)
#     Email=db.Column(db.String(50),nullable=True,unique=True)
#     links = db.relationship('Links', backref='owner', lazy=True)

def CreateAccount(username,password,email):
    info=__TransferingDB(username=username,password=password,email=email)
    Tosend=dict()
    Statuscode=200
    if info[0]==1:
        Tosend={
            "Status":"Success",
            "Report":"Go",
            "Userid":info[1]
            }
        
    elif info[0]==-1:
        Tosend={
            "Status":"Fail",
            "Report":str(info[1]),
            "Userid":-1}
        Statuscode=400
    elif info[0]==0:
        Tosend={
            "Status":"Fail",
            "Report":str(info[1]),
            "Userid":-1}
        Statuscode=400
    return Tosend,Statuscode



def __TransferingDB(username,password,email):
        password=__Hashing(Password=password) #Not gonna show in this repo for safety 
        Data=User(Username=username,Password=password,Email=email)
        try:
            db.session.add(Data)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return [-1,"The user Already Exist"]
        
        except Exception as e:
            db.session.rollback()
            ##Log this 
            return [0,e]
        Userid=Data.id
        return [1,Userid]

   



if __name__=="__main__":
    print(__Hashing("HEllo"))


