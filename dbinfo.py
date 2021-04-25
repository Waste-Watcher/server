from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import secrets

conn = "mysql+pymysql://{0}:{1}@{2}{3}".format(secrets.dbhost,secrets.dbuser,secrets.dbemail) 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)