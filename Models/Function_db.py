from Models.DB import USER

class Foodkart_Database(object):
    def __init__(self):
        pass

    def get_user(self):
        users = self.SESSIONS.query(USER).all()
        user_dict = {}
        for user in users:
            user_dict.update({user.id, user.name})

        return user_dict