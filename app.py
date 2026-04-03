from flask import Flask
from models.LoginSql import db
from models.LinksTable import Links #Just so the table is  created early
from dotenv import load_dotenv
import os 
from routes.LoginPage.Login import LoginBP
load_dotenv()
app=Flask(__name__)

DatbaseUserName=os.getenv("DatbaseUserName")
DatabasePassword=os.getenv("DatabasePassword")
DatabaseHost=os.getenv("DatabaseHost")
DatabaseName=os.getenv("DataBaseName")

try:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DatbaseUserName}:{DatabasePassword}@{DatabaseHost}/{DatabaseName}"
    #  app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{Database}@localhost/tapnap"
except Exception as e:
    print(e)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' ##Trace back Database

app.secret_key=os.getenv("SECRETKEY")
db.init_app(app)
app.register_blueprint(LoginBP)
try:
    with app.app_context():
            db.create_all()
except Exception as e:
    print(e)

if __name__=="__main__":

    app.run()
    # print()