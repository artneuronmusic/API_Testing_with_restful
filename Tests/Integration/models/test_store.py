from Models.store import StoreModel
from Models.item import ItemModel
from Tests.base_test import BaseTest


class StoreTest(BaseTest):

    def test_create_store_items_empty(self):
        store = StoreModel("Costco")

        self.assertListEqual(store.items.all(), [])


    def test_crud(self):

        with self.app_context():
            store = StoreModel("Costco")
            self.assertIsNotNone(store.name)
            self.assertIsNone(StoreModel.find_by_name("Costco"))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name("Costco"))

            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name("Costco"))


    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("Costco")
            item = ItemModel("ham", "20.11", 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, "ham")
            self.assertEqual(store.items.first().price, 20.11)


    def test_json(self):
        store = StoreModel('Costco')
        expected = {"name": "Costco", "item_list": []}

        self.assertDictEqual(store.json(), expected)


    def test_json_with_item(self):
        with self.app_context():
            store = StoreModel("Costco")
            item = ItemModel("ham", 20.11, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {"name": "Costco", "item_list": [{"name": "ham", "price": 20.11}]}

            self.assertDictEqual(store.json(), expected)







