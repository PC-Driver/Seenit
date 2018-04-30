import os
import sqlite3 as sql
import user, db, seenit, post, comment
import postUpvote as pu
import postDownvote as pd
import commentUpvote as cu
import commentDownvote as cd

new_u_id = new_s_id = new_p_id = new_c_id = 5
new_pu_id = 8
new_pd_id = new_cu_id = new_cd_id = 1
this_u_id = 0

# run this when database is not created yet
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
2 = Already A Member
3 = Main Menu
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

def insert_seenit():
    global new_s_id
    category = input("Please describe your seenit.")
    seenit.insert(new_s_id,category,this_u_id)
    new_s_id += 1
    show_seenits()    

def show_seenit():
    s_id = input("Please input id of the one you choose:")
    _seenit = seenit.read_one(s_id)
    print (_seenit)
    posts = post.read_all(s_id)
    print ("Posts:")
    print (posts)
    # post menu

def delete_seenit():
    s_id = input("Please input id of the one you choose:")
    seenit.delete(s_id)
    show_seenits()

def update_seenit():
    s_id = input("Please input id of the one you choose:")
    category = input("Please describe your seenit.")
    seenit.update(s_id,category)
    show_seenits()

def show_seenits():  
    seenits = seenit.read_all()
    print (seenits)
    print("-" * 40)
    print ("                Seenit Menu")
    print("-" * 40)
    method = input('''   
        1 = Create One
        2 = Choose One
        3 = Delete One
        4 = Update One
        5 = Main Menu
        6 = Exit
        ''')
    if method == '1':
        insert_seenit()
    elif method == '2':
        show_seenit()
    elif method == '3':
        delete_seenit()
    elif method == '4':
        update_seenit();
    elif method == '6':
        exit()
    else:
        main_menu()

# def account_profile():
#     print("-" * 40)
#     print ("                Account Menu")
#     print("-" * 40)    
#     method = input('''   
#         1 = My Seenits
#         2 = My Posts
#         3 = My Comments
#         4 = My Upvoted Posts
#         5 = My Downvoted Posts
#         6 = My Upvoted Comments
#         7 = My Downvoted Comments
#         8 = Main Menu
#         9 = Exit
#         ''')

def main_menu():
    # while True:
        print("-" * 40)
        print ("                Main Menu")
        print("-" * 40)
        print ("User ID is", this_u_id)
        print ("0 means not logged in yet, other number means logged in already")
        if this_u_id:
            method = input(''' 
                0 = Account Profile  
                2 = Show Seenits
                3 = Exit
                ''')
        else:    
            method = input('''   
                1 = Login
                3 = Exit
                ''')
        if method == '1':
            login()
        elif method == '2':
            show_seenits()
        # elif method == '0':
        #     account_profile()
        else:
            exit()

main_menu()