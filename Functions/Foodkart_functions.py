from Models.Function_db import Foodkart_Database
from Requirements.Foodkart_user import USER
from Requirements.Kart import kart

class FoodKartControl(object):

    def __init__(self):
        self.kart = kart()
        self.users = self.kart.all_users()
        self.restaurants = self.kart.all_restaurants()


    def add_user(self,id,name,phone_number,gender,pincode):
        all_users_id = [user.id for user in self.users]
        if id in all_users_id:
            return "User already exist"
        else:
