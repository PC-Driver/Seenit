import os
import sqlite3 as sql
import user, db, seenit, post, comment
import logging as f
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
    f.writing("Build database\n")
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
    f.writing("Register request user response\n")
    print("1 - Register")
    x = input("user name: ")
    z = input("password: ")
    y = input("email: ")
    w = input("Are you an administrator? (y/n)")
    f.writing("Response: ")
    f.writing("user name: ")
    f.writing(x)
    f.writing(" password: ")
    f.writing(z)
    f.writing(" email: ")
    f.writing(y)
    f.writing("Are you administrator? ")
    f.writing(w)
    f.writing("\n")
    user.insert(new_u_id, x, z, y)
    this_u_id = new_u_id
    # print ("this u id is ", this_u_id)
    new_u_id += 1
    if w == 'y':
        admin = True
    main_menu()


def login():
    global this_u_id, admin
    f.writing("Print login menu - Request user response\n")
    print("-" * 40)
    print("               Login Menu")
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
        f.writing("Response: 1 - Register\n")
        register()
    elif login == '2':
        f.writing("Response: 2 - Already A Member\n")
        f.writing("Print login menu - Request user response\n")
        print("2 - Login")
        x = input("user name:")
        y = input("password:")
        w = input("Are you an administrator? (y/n)")
        this_u_id = user.login(x, y)
        f.writing("user name: ")
        f.writing(x)
        f.writing(" password: ")
        f.writing(y)
        f.writing(" Are you an administrator? ")
        f.writing(w)
        f.writing("\n")
        if w == 'y':
            admin = True
        main_menu()
    elif login == '3':
        f.writing("Response: 3 - main menu\n")
        main_menu()
    else:
        f.writing("Response: 4 - Exit\n")
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
    f.writing("delete_vote request user response: Please input id of the one you want to delete\n")
    v_id = input("Please input id of the one you want to delete:")
    f.writing("Response: ")
    f.writing(v_id)
    f.writing("\n")
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
    print("Upvotes:")
    print(up)
    if table == 'comment':
        down = cd.read_all(id)
    else:
        down = pd.read_all(id)
    print("Downvotes:")
    print(down)
    print("-" * 40)
    print("                Vote Menu")
    print("-" * 40)
    f.writing("Print show_votes menu - Request user's response\n")
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
        f.writing("Response: 1 - Up\n")
        insert_vote(table, 'up', id)
    elif method == '2':
        f.writing("Response: 2 - Down\n")
        insert_vote(table, 'down', id)
    elif method == '3':
        f.writing("Response: 3 - Delete Up\n")
        delete_vote(table, 'up', id)
    elif method == '4':
        f.writing("Response: 4 - Delete Down\n")
        delete_vote(table, 'down', id)
    elif method == '6':
        f.writing("Response: 6 - Exit")
        exit()
    else:
        f.writing("Response: 5 - Main Menu")
        main_menu()


def insert_comment(p_id):
    global new_c_id
    f.writing("insert_comment request user response - Please input your comment\n")
    content = input("Please input your comment:")
    f.writing("Response: ")
    f.writing(content)
    f.writing("\n")
    comment.insert(new_c_id, content, p_id, this_u_id)
    new_c_id += 1
    show_comments(p_id)


def show_comment(c_id):
    _comment = comment.read_one(c_id)
    print(_comment)
    show_votes('comment', c_id)


def delete_comment(p_id):
    f.writing("delete_comment request user response - Please input id of the one you choose\n")
    c_id = input("Please input id of the one you choose:")
    f.writing("Response: ")
    f.writing(c_id)
    f.writing("\n")
    comment.delete(c_id)
    show_comments(p_id)


def update_comment(p_id):
    f.writing("update_comment request user response - Please input the id of the one you choose\n")
    c_id = input("Please input id of the one you choose:")
    f.writing("Response: ")
    f.writing(c_id)
    f.writing("\n")
    f.writing("update_comment request user response - Please input your comment\n")
    content = input("Please input your comment:")
    f.writing("Response: ")
    f.writing(content)
    f.writing("\n")
    comment.update(c_id, content)
    show_comments(p_id)


def show_comments(p_id):
    comments = comment.read_all(p_id)
    print("Comments:")
    print(comments)
    print("-" * 40)
    print("                Comment Menu")
    print("-" * 40)
    f.writing("Print show_comments menu - Request user response\n")
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
        f.writing("Response: 1 - Create One\n")
        insert_comment(p_id)
    elif method == '2':
        f.writing("Response: 2 - Choose One\n")
        c_id = input("Please input id of the one you choose:")
        show_comment(c_id)
    elif method == '3':
        f.writing("Response: 3 - Delete One\n")
        delete_comment(p_id)
    elif method == '4':
        f.writing("Response: 4 - Update One\n")
        update_comment(p_id);
    elif method == '6':
        f.writing("Response: 6 - Exit\n")
        exit()
    else:
        f.writing("Response: 5 - Main Menu\n")
        main_menu()


def insert_post(s_id):
    global new_p_id
    f.writing("insert_post request user response - Please input your post\n")
    content = input("Please input your post:")
    f.writing("Response: ")
    f.writing(content)
    f.writing("\n")
    post.insert(new_p_id, content, s_id, this_u_id)
    new_p_id += 1
    show_posts(s_id)


def show_post():
    f.writing("show_post request user response - Please input id of the one you choose\n")
    p_id = input("Please input id of the one you choose:")
    f.writing("Response: ")
    f.writing(p_id)
    f.writing("\n")
    _post = post.read_one(p_id)
    print(_post)
    comment_and_vote_menu(p_id)


def comment_and_vote_menu(p_id):
    print("-" * 40)
    print("                Comment/Vote Menu")
    print("-" * 40)
    f.writing("Print comment_and_vote_menu menu - Request user response\n")
    method = input('''   
        1 = Show Comments
        2 = Show Votes
        3 = Main Menu
        4 = Exit
        ''')
    if method == '1':
        f.writing("Response: 1 - Show Comments\n")
        show_comments(p_id)
    elif method == '2':
        f.writing("Response: 2 - Show votes\n")
        show_votes('post', p_id)
    elif method == '4':
        f.writing("Response: 4 - Exit\n")
        exit()
    else:
        f.writing("Response: 3 - Main Menu\n")
        main_menu()


def delete_post(s_id):
    p_id = input("Please input id of the one you choose:")
    post.delete(p_id)
    show_posts(s_id)


def update_post(s_id):
    f.writing("update_post request user response - Please input id of the one you choose\n")
    p_id = input("Please input id of the one you choose:")
    f.writing("Response: ")
    f.writing(p_id)
    f.writing("\n")
    f.writing("update_post request usr response - Please input your post\n")
    content = input("Please input your post:")
    f.writing("Reponse: ")
    f.writing(content)
    f.writing("\n")

    post.update(p_id, content)
    show_posts(s_id)


def show_posts(s_id):
    posts = post.read_all(s_id)
    print("Posts:")
    print(posts)
    print("-" * 40)
    print("                Post Menu")
    print("-" * 40)
    f.writing("Print show_posts menu - Request user response\n")
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
        f.writing("Response: 1 - Create One\n")
        insert_post(s_id)
    elif method == '2':
        f.writing("Response: 2 - Choose One\n")
        show_post()
    elif method == '3':
        f.writing("Response: 3 - Delete One\n")
        delete_post(s_id)
    elif method == '4':
        f.writing("Response: 4 - Update One\n")
        update_post(s_id);
    elif method == '6':
        f.writing("Response: 6 - Exit\n")
        exit()
    else:
        f.writing("Response: 5 - Main Menu\n")
        main_menu()


def insert_seenit():
    global new_s_id
    f.writing("insert_seenit request user response - Please describe your seenit\n")
    category = input("Please describe your seenit:")
    f.writing("Response: ")
    f.writing(category)
    f.writing("\n")
    seenit.insert(new_s_id, category, this_u_id)
    new_s_id += 1
    show_seenits()


def show_seenit():
    f.writing("show_seenit request user reponse - Please input id of the one you choose\n")
    s_id = input("Please input id of the one you choose:")
    f.writing("Response: ")
    f.writing(s_id)
    f.writing("\n")
    _seenit = seenit.read_one(s_id)
    print(_seenit)
    show_posts(s_id)


def delete_seenit():
    f.writing("delete_seenit request user reponse - Please input id of the one you choose\n")
    s_id = input("Please input id of the one you choose:")
    f.writing("Response: ")
    f.writing(s_id)
    f.writing("\n")
    seenit.delete(s_id)
    show_seenits()


def update_seenit():
    f.writing("update_seenit request user response - Please input id of the one you choose\n")
    s_id = input("Please input id of the one you choose:")
    f.writing("Response: ")
    f.writing(s_id)
    f.writing("\n")
    f.writing("update_seenit request user response - Please decribe your seenit\n")
    category = input("Please describe your seenit:")
    f.writing("Response: ")
    f.writing(category)
    f.writing("\n")
    seenit.update(s_id, category)
    show_seenits()


def show_seenits():
    seenits = seenit.read_all()
    print(seenits)
    print("-" * 40)
    print("                Seenit Menu")
    print("-" * 40)
    f.writing("Print show_seenits menu - Request user reponse\n")
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
        f.writing("Response: 1 - Create One\n")
        insert_seenit()
    elif method == '2':
        f.writing("Response: 2 - Choose One\n")
        show_seenit()
    elif method == '3':
        f.writing("Response: 3 - Delete One\n")
        delete_seenit()
    elif method == '4':
        f.writing("Response: 4 - Update One\n")
        update_seenit();
    elif method == '6':
        f.writing("Response: 6 - Exit\n")
        exit()
    else:
        f.writing("Response: 5 - Main Menu\n")
        main_menu()


def account_profile():
    global this_u_id
    user_info = user.read_one(this_u_id)
    print("Account Information:")
    print(user_info)
    print("-" * 40)
    print("                Account Menu")
    print("-" * 40)
    f.writing("Print account_profile menu - Request user response\n")
    if admin == True:
        method = input('''   
            1 = Update My Account Info
            2 = Delete My Account
            3 = Show All Accounts
            4 = Main Menu
            5 = Exit
            ''')
    else:
        method = input('''   
            1 = Update My Account Info
            2 = Delete My Account
            4 = Main Menu
            5 = Exit
            ''')
    if method == '1':
        f.writing("Response: 1 - Update Account Info\n")
        f.writing("Response 1 request user response\n")
        x = input("user name: ")
        z = input("password: ")
        y = input("email: ")
        f.writing("user name: ")
        f.writing(x)
        f.writing(" password: ")
        f.writing(z)
        f.writing(" email: ")
        f.writing(y)
        f.writing("\n")
        user.update(this_u_id, x, z, y)
        account_profile()
    elif method == '2':
        f.writing("Response: 2 - Delete My Account\n")
        user.delete(this_u_id)
        this_u_id = 0
        main_menu()
    elif method == '3':
        f.writing("Response: 3 - Show All Accounts\n")
        all_users = user.read_all()
        print(all_users)
        account_profile()
    elif method == '5':
        f.writing("Response: 5 - Exit\n")
        exit()
    else:
        f.writing("Response: 4 - Main Menu\n")
        main_menu()


def main_menu():
    print("-" * 40)
    print("                Main Menu")
    print("-" * 40)
    print("User ID is", this_u_id)
    print("0 means not logged in yet, other number means logged in already")
    f.writing("Printing main menu - Request user response\n")
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
        f.writing("Response: 1 - Login\n")
        login()
    elif method == '2':
        f.writing("Response: 2 - Show Seenits\n")
        show_seenits()
    elif method == '0':
        f.writing("Response: 0 - Account Profile\n")
        account_profile()
    else:
        f.writing("Response: 3 - Exit\n")
        exit()


# build_database()
main_menu()
f.closing()