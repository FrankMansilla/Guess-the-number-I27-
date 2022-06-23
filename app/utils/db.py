import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

Base = SQLAlchemy()

cnx_user = 'frank' 
cnx_pass = '123456'
cnx_host = 'localhost'
cnx_db   = 'testsqlalchemy'
conenxion_str = cnx_user+':'+cnx_pass+'@'+cnx_host+'/'+cnx_db
engine = create_engine("mysql+pymysql://"+conenxion_str+"?charset=utf8mb4")