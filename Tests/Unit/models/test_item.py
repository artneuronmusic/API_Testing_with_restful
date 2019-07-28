#from unittest import TestCase


import os
import sys
sys.path.append(os.path.join(os.path.dirname("__file__"), "..", "..", ".."))

from Tests.Unit.unit_base_test import UnitBaseTest
from Models.item import ItemModel
#from Models.store import StoreModel     python later on will complain
#from Tests.base_test import BaseTest   =>originally it was in Tests

#class ItemTest(TestCase):
#class ItemTest(BaseTest): this one will slow everything down, it will start up everything
class ItemTest(UnitBaseTest):

    def test_create_item(self):
        item = ItemModel("cookies", 19.88, 1)
        self.assertEqual(item.name, "cookies")
        self.assertEqual(item.price, 19.88)
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)



    def test_item_json(self):
        item = ItemModel("cookies", 19.88, 1)
        self.assertDictEqual(item.json(), {"name": "cookies", "price": 19.88})

