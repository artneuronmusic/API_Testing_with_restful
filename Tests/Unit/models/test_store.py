from Tests.Unit.unit_base_test import UnitBaseTest
from Models.store import StoreModel


class TestStoreModel(UnitBaseTest):

    def test_create_store(self):
        store = StoreModel("Costco")

        self.assertEqual(store.name, "Costco")

    def test_json(self):
        store = StoreModel('Costco')
        expected = {"name": "Costco", "item_list": []}

        self.assertDictEqual(store.json(), expected)


