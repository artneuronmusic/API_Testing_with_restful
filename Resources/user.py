from flask_restful import Resource, reqparse
from Models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username",
                         type=str,
                         required=True,
                         help="This field can't be blank")
    parser.add_argument("password",
                         type=str,
                         required=True,
                         help="This field can't be blank")



    def post(self):

        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "the account is used by someone already"}, 400

        user_account = UserModel(**data)
        user_account.save_to_db()

        return {"message": "the account register successfully"}, 201



