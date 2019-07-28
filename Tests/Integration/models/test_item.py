from Tests.base_test import BaseTest
from Models.item import ItemModel
from Models.store import StoreModel

class ItemTest(BaseTest):

    def test_crud(self):

        with self.app_context():

            StoreModel("COSTCO").save_to_db #save COSTCO to the database in order to deal with foreigner key
            item = ItemModel("cookies", 19.98, 1) #test the foreign key
            self.assertIsNone(ItemModel.find_by_name("cookies"))
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name("cookies"))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name("cookies"))


    def test_store_relationship(self):

        with self.app_context():
            store_label=StoreModel("Costco")
            item=ItemModel("cookies", 19.87, 1)
            store_label.save_to_db()
            item.save_to_db()
            self.assertEqual(item.store.name, "Costco")
            #(object.relationship.relationship property)







