from werkzeug.security import safe_str_cmp
from Models.user import UserModel

def authenticate(username, password):

    """prepare password, username in string format to call the /auth endpoint"""

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

    return None



def identity(payload):
    """if the user is authenticated, Flask-JWT is verified their authorization header is correct"""
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)