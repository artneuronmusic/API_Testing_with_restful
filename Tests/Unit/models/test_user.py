from Models.user import UserModel
from Tests.Unit.unit_base_test import UnitBaseTest
#from unittest import TestCase

class UserTest(UnitBaseTest):

    def test_create_user(self):
        new = UserModel("ipo", "kkk123")

        self.assertEqual(new.username, "ipo")

        self.assertEqual(new.password, "kkk123")
