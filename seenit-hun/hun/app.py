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
admin = False

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
    global new_u_id, this_u_id, admin
    print("1 - Register")
    x = input("user name: ")
    z = input("password: ")
    y = input("email: ")
    w = input("Are you an administrator? (y/n)")
    user.insert(new_u_id, x, z, y)
    this_u_id = new_u_id
    # print ("this u id is ", this_u_id)
    new_u_id += 1
    if w == 'y':
        admin = True
    main_menu()  

def login():
    global this_u_id, admin
    print_register_menu()
    login = input()

    # print("\n")
    if login == '1':
        register()
    elif login == '2':
        print("2 - Login")
        x = input("user name:")
        y = input("password:")
        w = input("Are you an administrator? (y/n)")
        this_u_id = user.login(x, y)
        if w == 'y':
            admin = True
        main_menu()
    elif login == '3':
        main_menu()
    else:
        exit()  

def insert_vote(table, vote, id):
    global new_pu_id, new_pd_id, new_cu_id, new_cd_id
    if table == 'post':
        if vote == 'up':
            pu.insert(new_pu_id, id, this_u_id)
            new_pu_id += 1
        else:
            pd.insert(new_pd_id, id, this_u_id)
            new_pd_id += 1
        # show_post(id)
    else:
        if vote == 'up':
            cu.insert(new_cu_id, id, this_u_id)
            new_cu_id += 1
        else:
            cd.insert(new_cd_id, id, this_u_id)
            new_cd_id += 1
        show_comment(id)        

def delete_vote(table, vote, id):
    v_id = input("Please input id of the one you want to delete:")
    if table == 'post':
        if vote == 'up':
            pu.delete(v_id)
        else:
            pd.delete(v_id)
        show_votes('post', id)
    else:
        if vote == 'up':
            cu.delete(v_id)
        else:
            cd.delete(v_id)
        show_comment(id)

def show_votes(table, id):
    if table == 'comment':
        up = cu.read_all(id)
    else:
        up = pu.read_all(id)
    #print ("Upvotes:")
    print (up)
    if table == 'comment':
        down = cd.read_all(id)
    else:
        down = pd.read_all(id)
    #print ("Downvotes:")
    print (down)
    print("-" * 40)
    print ("                Vote Menu")
    print("-" * 40)
    if admin == True:
        method = input('''   
            1 = Up
            2 = Down
            3 = Delete Up
            4 = Delete Down
            5 = Main Menu
            6 = Exit
            ''')
    else:
        method = input('''   
            1 = Up
            2 = Down
            5 = Main Menu
            6 = Exit
            ''')
    if method == '1':
        insert_vote(table, 'up', id)
    elif method == '2':
        insert_vote(table, 'down', id)
    elif method == '3':
        delete_vote(table, 'up', id)
    elif method == '4':
        delete_vote(table, 'down', id)
    elif method == '6':
        exit()
    else:
        main_menu()

def insert_comment(p_id):
    global new_c_id
    content = input("Please input your comment:")
    comment.insert(new_c_id,content,p_id,this_u_id)
    new_c_id += 1
    show_comments(p_id)  

def show_comment(c_id):
    _comment= comment.read_one(c_id)
    print (_comment)
    show_votes('comment', c_id)

def delete_comment(p_id):
    c_id = input("Please input id of the one you choose:")
    comment.delete(c_id)
    show_comments(p_id)

def update_comment(p_id):
    c_id = input("Please input id of the one you choose:")
    content = input("Please input your comment:")
    comment.update(c_id,content)
    show_comments(p_id)

def show_comments(p_id):
    comments = comment.read_all(p_id)
    #print ("Comments:")
    print (comments)
    print("-" * 40)
    print ("                Comment Menu")
    print("-" * 40)
    if admin == True:
        method = input('''   
            1 = Create comment
            2 = Choose comment
            3 = Delete comment
            4 = Update comment
            5 = Main Menu
            6 = Exit
            ''')
    else:
        method = input('''   
            1 = Create comment
            2 = Choose comment
            5 = Main Menu
            6 = Exit
            ''')        
    if method == '1':
        insert_comment(p_id)
    elif method == '2':
        c_id = input("Please input id of the one you choose:")
        show_comment(c_id)
    elif method == '3':
        delete_comment(p_id)
    elif method == '4':
        update_comment(p_id);
    elif method == '6':
        exit()
    else:
        main_menu()

def insert_post(s_id):
    global new_p_id
    content = input("Please input your post:")
    post.insert(new_p_id,content,s_id,this_u_id)
    new_p_id += 1
    show_posts(s_id)  

def show_post():
    p_id = input("Please input id of the one you choose:")
    _post= post.read_one(p_id)
    print (_post)
    comment_and_vote_menu(p_id)
    
def comment_and_vote_menu(p_id):
    print("-" * 40)
    print ("                Comment/Vote Menu")
    print("-" * 40)
    method = input('''   
        1 = Show Comments
        2 = Show Votes
        3 = Main Menu
        4 = Exit
        ''')
    if method == '1':
        show_comments(p_id)
    elif method == '2':
        show_votes('post', p_id)
    elif method == '4':
        exit()
    else:
        main_menu()    

def delete_post(s_id):
    p_id = input("Please input id of the one you choose:")
    post.delete(p_id)
    show_posts(s_id)

def update_post(s_id):
    p_id = input("Please input id of the one you choose:")
    content = input("Please input your post:")
    post.update(p_id,content)
    show_posts(s_id)

def show_posts(s_id):
    posts = post.read_all(s_id)
    #print ("Posts:")
    print (posts)
    print("-" * 40)
    print ("                Post Menu")
    print("-" * 40)
    if admin == True:
        method = input('''   
            1 = Create post
            2 = Choose post
            3 = Delete post
            4 = Update post
            5 = Main Menu
            6 = Exit
            ''')
    else:
        method = input('''   
            1 = Create post
            2 = Choose post
            5 = Main Menu
            6 = Exit
            ''') 
    if method == '1':
        insert_post(s_id)
    elif method == '2':
        show_post()
    elif method == '3':
        delete_post(s_id)
    elif method == '4':
        update_post(s_id);
    elif method == '6':
        exit()
    else:
        main_menu()

def insert_seenit():
    global new_s_id
    category = input("Please describe your seenit:")
    seenit.insert(new_s_id,category,this_u_id)
    new_s_id += 1
    show_seenits()    

def show_seenit():
    s_id = input("Please input id of the one you choose:")
    _seenit = seenit.read_one(s_id)
    print (_seenit)
    show_posts(s_id)

def delete_seenit():
    s_id = input("Please input id of the one you choose:")
    seenit.delete(s_id)
    show_seenits()

def update_seenit():
    s_id = input("Please input id of the one you choose:")
    category = input("Please describe your seenit:")
    seenit.update(s_id,category)
    show_seenits()

def show_seenits():  
    seenit.read_all()
    print("-" * 40)
    print ("                Seenit Menu")
    print("-" * 40)
    if admin == True:
        method = input('''   
            1 = Create One
            2 = Choose One
            3 = Delete One
            4 = Update One
            5 = Main Menu
            6 = Exit
            ''')
    else:
        method = input('''   
            1 = Create One
            2 = Choose One
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

def account_profile():
    global this_u_id
    user_info = user.read_one(this_u_id)
    print("Account Information:")
    print(user_info)
    print("-" * 40)
    print ("                Account Menu")
    print("-" * 40)
    if admin == True:            
        method = input('''   
            1 = Update My Account Info
            2 = Delete My Account
            3 = Show All Accounts
            4 = Main Menu
            5 = Delete Accounts
            6 = Exit
            ''')
    else:
        method = input('''   
            1 = Update My Account Info
            2 = Delete My Account
            4 = Main Menu
            6 = Exit
            ''')
    if method == '1':
        x = input("user name: ")
        z = input("password: ")
        y = input("email: ")
        user.update(this_u_id, x, z, y)
        account_profile()
    elif method == '2':
        user.delete(this_u_id)
        this_u_id = 0
        main_menu()
    elif method == '3':
        all_users = user.read_all()
        print (all_users)
        account_profile()
    elif method == '5':
        x = input("Enter the ID of the account you want to delete")
        user.delete(x)
        account_profile()
    elif method == '6':
        exit()
    else:
        main_menu()

def logout():
    global this_u_id
    this_u_id = 0
    main_menu()

def print_main_menu():
    # MENU DESIGN!
    print 28 * "-", "MAIN MENU", 33 * "-"
    print '|', 25 * " ", "0. Account Profile", 23 * " ", "|"
    print '|', 25 * " ", "2. Show Seenits", 26 * " ", "|"
    print '|', 25 * " ", "3. Logout", 32 * " ", "|"
    print '|', 25 * " ", "4. Exit", 34 * " ", "|"
    print (72 * "-")

def print_Welcome_menu():
    # MENU DESIGN!
    print 30 * "~", "Welcome", 33 * "~"
    print '|', 25 * " ", "User ID is", this_u_id, 29 * " ", "|"
    print '|', 2 * " ", "0 means not logged in yet, other number means logged in already", 1 * " ", "|"
    print (72 * "~")

def print_login_menu():
    # MENU DESIGN!
    print 28 * "-", "MAIN MENU", 33 * "-"
    print '|', 25 * " ", "1. Login", 33 * " ", "|"
    print '|', 25 * " ", "4. exit", 34 * " ", "|"
    print (72 * "-")

def print_register_menu():
    # MENU DESIGN!
    print 27 * "-", "LOGIN MENU", 33 * "-"
    print '|', 25 * " ", "1. Register", 30 * " ", "|"
    print '|', 25 * " ", "2. Already A Member", 22 * " ", "|"
    print '|', 25 * " ", "3. Main Menu", 29 * " ", "|"
    print '|', 25 * " ", "4. Exit", 34 * " ", "|"
    print (72 * "-")

def main_menu():
    logging.info("Printing main menu - Request user response\n")
    print_Welcome_menu()
    if this_u_id:
        print_main_menu()
        method = input()
    else:
        print_login_menu()
        method = input()
    if method == '1':
        logging.info("Response: 1 - Login\n")
        login()
    elif method == '2':
        logging.info("Response: 2 - Show Seenits\n")
        show_seenits()
    elif method == '0':
        logging.info("Response: 0 - Account Profile\n")
        account_profile()
    elif method == '3':
        logging.info("Response: 3 - Logout\n")
        logout()
    elif method == '5':
        logging.info("Response: 5 - Show Users\n")
        show_users()
        
    else:
        logging.info("Response: 3 - Exit\n")
        exit()

build_database()
main_menu()