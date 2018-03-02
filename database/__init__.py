from database import DB, Querys

# DB.py
db = DB.db

# Querys.py
def Get_user(u):
    return Querys._Find_user(u)
def New_user(u, pw):
    return Querys._Create_user(u, pw)
def Username_used(u):
    return Querys._Check_username_used(u)
def Reset_password(u, pw):
    return Querys._Reset_user_password(pw, u)