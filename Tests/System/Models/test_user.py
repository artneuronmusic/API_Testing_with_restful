from Models.user import UserModel
from Tests.base_test import BaseTest
import json


class UserTest(BaseTest):

    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                response = client.post("/register", data={"username": "ipo", "password": "ko123"})
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username("ipo"))
                self.assertIsNotNone(UserModel.find_by_id(1))
                self.assertDictEqual({"message": "the account register successfully"}, json.loads(response.data))
     #loads =>decode
     #dumps =>encode

    def test_register_login(self):
        with self.app() as client:
            with self.app_context():
                client.post("/register", data={"username": "ipo", "password": "ko123"})
                auth_response = client.post("/auth", data=json.dumps({"username": "ipo", "password": "ko123"}),
                                           headers={"Content-Type": "application/json"})

                self.assertIn("access_token", json.loads(auth_response.data).keys())


    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                client.post("/register", data={"username": "ipo", "password": "ko123"})
                response = client.post("/register", data={"username": "ipo", "password": "ko123"})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({"message": "the account is used by someone already"}, json.loads(response.data))

