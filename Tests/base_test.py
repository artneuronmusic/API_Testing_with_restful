from unittest import TestCase
from app import app
from db import db



class BaseTest(TestCase):

    # set up database and get testclient and make sure databse exists
    # after test, the data bse is completely blank

    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"  # new blank database
        app.config["DEBUG"] = False  #react to db,init_app(app)
        app.config["PROPAGATE_EXCEPTION"] = True #react to db,init_app(app)
        with app.app_context():
            db.init_app(app) #flask might have problem with it



    def setUp(self):
        #app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" #new blank database
        with app.app_context():
            #db.init_app(app)
            db.create_all() #we need to create table everytime

        self.app = app.test_client
        self.app_context = app.app_context



    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

