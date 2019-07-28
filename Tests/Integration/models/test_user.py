
from Models.user import UserModel
from Tests.base_test import BaseTest

class UserTest(BaseTest):

    def test_crud(self):
        with self.app_context():
            user = UserModel("ipo", "kk")

            self.assertIsNone(UserModel.find_by_username("ipo"))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()
            self.assertIsNotNone(UserModel.find_by_username("ipo"))
            self.assertIsNotNone(UserModel.find_by_id(1))








