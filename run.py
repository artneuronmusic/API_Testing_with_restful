#import os, sys
#sys.path.append(os.path.join(os.path.dirname("__file__"), ".."))
from app import app
from .db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

