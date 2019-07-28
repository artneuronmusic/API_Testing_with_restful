from Models.store import StoreModel
from Models.item import ItemModel
from Tests.base_test import BaseTest
import json

class StoreTest(BaseTest):



    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post("/store/costco")

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name("costco"))
                self.assertDictEqual({"name": "costco", "item_list": []}, json.loads(response.data))



    def test_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post("/store/costco")
                response = client.post("/store/costco")

                self.assertEqual(response.status_code, 400)



    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                #client.post("/store/costco")
                StoreModel("Costco").save_to_db()
                response = client.delete("/store/costco")

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({"message": "Store deleted"}, json.loads(response.data))


    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("Costco").save_to_db()
                response = client.get("store/Costco")

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({"name": "Costco", "item_list": []}, json.loads(response.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():

                response = client.get("store/Costco")

                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'}, json.loads(response.data))



    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("Costco").save_to_db()
                ItemModel("ham", 19.99, 1).save_to_db()
                response = client.get("store/Costco")

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({"name": "Costco", "item_list": [{"name": "ham", "price": 19.99}]}, json.loads(response.data))


    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("Costco").save_to_db()
                response = client.get("stores")

                self.assertDictEqual({"stores": [{"name": "Costco", "item_list": []}]},
                                     json.loads(response.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("Costco").save_to_db()
                ItemModel("ham", 19.99, 1).save_to_db()
                response = client.get("stores")

                self.assertDictEqual({"stores": [{"name": "Costco", "item_list": [{"name": "ham", "price": 19.99}]}]},
                                     json.loads(response.data))
