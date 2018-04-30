import os
import sqlite3 as sql
from dbs import user,db,seenit
# from dbs import db

new_u_id = 6
this_u_id

def build_database():
    db.create_tables()
    db.insert_users()
    db.insert_seenits()
    db.insert_posts()
    db.insert_comments()
    db.insert_post_upvote()
    db.show_seenits()
    db.show_posts()
    db.show_comments()
    db.show_post_upvotes()
        
def register():
    global new_u_id
    print("1 - Register")
    x = input("user name?")
    y = input("email?")
    user.insert(new_u_id, x, y)
    new_u_id += 1    

def login():
    global this_u_id
    while True:
        print("-" * 40)
        print ("               Login Menu")
        print("-" * 40)
        login = input('''
    1 = Register
    2 = Login
    3 = Back
    4 = Exit
        ''')
        print("-" * 40)
        # print("\n")
        if login == 1:
            register()
            this_u_id = new_u_id - 1
        elif login == 2:
            print("2 - Login")
            x = input("user name?")
            this_u_id = user.show_user(x)
        elif login == 3:
            main_menu()
        else:
            break    

def show_seenits():
    seenits = seenit.show_seenits()
    print (seenits)



def main_menu():
    while True:
        print("-" * 40)
        print ("                Main Menu")
        print("-" * 40)
        method = input('''   
            1 = Login
            2 = Show Seenits
            3 = Exit
            ''')
        if method == 1:
            login()
        elif method == 2:
            show_seenits()
        else:
            break

build_database()
main_menu()