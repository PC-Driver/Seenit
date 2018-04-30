import os
import sqlite3 as sql
from dbs import user
from dbs import db

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
        

while True:
    build_database()
    global u_id
    u_id = 5
    print("-" * 40)
    print ("                Menu")
    print("-" * 40)
    method = input('''   
        1 = Login
        2 = Display Accounts
        3 = Modify
        4 = Exit
        ''')
    if method == 1:

        while True:
            print("-" * 40)
            print ("               Menu2")
            print("-" * 40)
            login = input('''
        1 = Create Account
        2 = Login
        4 = Exit
            ''')
            print("-" * 40)
            # print("\n")
            if login == 1:
                print("1 - Insert user")
                x = input("user name?")
                y = input("email?")
                user.insert(u_id, x, y)
                u_id += 1
            elif login == 2:
                print("2 - Login")
            else:
                break
    elif method == 2:
        users = user.show_users()
        print (users)
    else:
        break
