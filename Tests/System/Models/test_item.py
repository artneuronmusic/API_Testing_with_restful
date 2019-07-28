from Models.item import ItemModel
from Models.user import UserModel
from Models.store import StoreModel
from Tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp() #call BaseTest
        with self.app() as client:
            with self.app_context():
                UserModel("ipo", "koko123").save_to_db()

                auth_request = client.post("/auth", data=json.dumps({"username": "ipo", "password": "koko123"}),
                                           headers={"Content-Type": "application/json"})

                auth_token = json.loads(auth_request.data)['access_token']
                #header = {"Authorization": "JWT {}".format(auth_token)}
                self.access_token = "JWT {}".format(auth_token)


    #def test_item_no_auth(self):
     #   with self.app() as client:
            #with self.app_context():

      #          r = client.get('/item/test')
       #         self.assertEqual(r.status_code, 401)


    def test_get_item_not_found(self):
        with self.app() as client:
            #with self.app_context():

                response = client.get("/item/ham", headers={"Authorization": self.access_token})
                self.assertEqual(response.status_code, 404)



    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                #StoreModel("Costco").save_to_db()
                #StoreModel("Costco").save_to_db()
                ItemModel("ham", 18.29, 1).save_to_db()
                response = client.get("/item/ham", headers={"Authorization": self.access_token})
                self.assertEqual(response.status_code, 200)


    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                # StoreModel("Costco").save_to_db()
                StoreModel("Costco").save_to_db()
                ItemModel("ham", 18.29, 1).save_to_db()
                response = client.delete("/item/ham") #dont need authorization anymore
                self.assertEqual(response.status_code, 200)


    def test_create_item(self):
        with self.app() as client:
            with self.app_context():

                StoreModel("Costco").save_to_db()
                #ItemModel("ham", 18.29, 1).save_to_db()
                response = client.post("/item/ham", data={"price": 17.55, "store_id": 1})  # dont need authorization anymore
                self.assertEqual(response.status_code, 201)
                self.assertEqual(ItemModel.find_by_name('ham').price, 17.55)
                self.assertDictEqual({"name": "ham", "price": 17.55}, json.loads(response.data))


    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("Costco").save_to_db()
                ItemModel("ham", 18.29, 1).save_to_db()

                response = client.post("/item/ham", data={"price": 17.55, "store_id": 1})
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({"message": "the item already exists"}, json.loads(response.data))


    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("Costco").save_to_db()

                response = client.put("/item/ham", data={"price": 17.55, "store_id": 1})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name("ham").price, 17.55)



    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("Costco").save_to_db()
                ItemModel("ham", 18.29, 1).save_to_db()
                response = client.put("/item/ham", data={"price": 17.55, "store_id": 1})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name("ham").price, 17.55)

    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                with self.app_context():
                    StoreModel("Costco").save_to_db()
                    ItemModel("ham", 18.29, 1).save_to_db()

                    response = client.get("/items")
                    self.assertDictEqual(d1={'items': [{'name': 'ham', 'price': 18.29}]},
                                         d2=json.loads(response.data))