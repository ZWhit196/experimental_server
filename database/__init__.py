from models import User
from database import Querys

# Querys
def Get_user(e):
    return Querys._Find_user(e)
def New_user(e, pw):
    return Querys._Create_user(e, pw)
def Email_used(e):
    return Querys._Check_email_used(e)
def Reset_password(e, pw):
    return Querys._Reset_user_password(pw, e)