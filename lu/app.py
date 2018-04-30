import os
import sqlite3 as sql
import user,db,seenit

new_u_id = 6
this_u_id = 0

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
    global new_u_id, this_u_id
    print("1 - Register")
    x = input("user name?")
    y = input("email?")
    user.insert(new_u_id, x, y)
    this_u_id = new_u_id
    print ("this u id is ", this_u_id)
    new_u_id += 1  
    main_menu()  

def login():
    global this_u_id
    # while True:
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
        if login == '1':
            register()
        elif login == '2':
            print("2 - Login")
            x = input("user name?")
            this_u_id = user.read_one(x)
            main_menu()
        elif login == '3':
            main_menu()
        else:
            exit()  

def show_seenits():
    seenits = seenit.read_all()
    print (seenits)

def main_menu():
    # while True:
        print("-" * 40)
        print ("                Main Menu")
        print("-" * 40)
        print ("User ID is", this_u_id)
        if this_u_id:
            method = input('''   
                2 = Show Seenits
                3 = Exit
                ''')
        else:    
            method = input('''   
                1 = Login
                2 = Show Seenits
                3 = Exit
                ''')
        if method == '1':
            login()
        elif method == '2':
            show_seenits()
        else:
            exit()

build_database()
main_menu()