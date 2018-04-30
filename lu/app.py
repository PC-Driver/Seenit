import os
import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert_user(info):
    with conn:
        c.execute("INSERT INTO user VALUES (:u_id, :u_name, :email)",
                  {'u_id':info.u_id, 'u_name':info.u_name, 'email':info.email})

def print_menu():
        #MENU DESIGN!
        print (33* "-", "MENU" , 33 * "-")
        print( "|", 30 * " ", "insert user", 25 * " ", "|", )
        print( "|", 30 * " ", "insert subseenit", 20 * " ", "|", )
        print( "|", 30 * " ", "modify", 30 * " ", "|", )
        print( "|", 30 * " ", "delete", 30 * " ", "|", )
        print( "|", 30 * " ", "display tables", 22 * " ", "|", )
        print( "|", 30 * " ", "exit", 32 * " ", "|", )
        print (72* "-")

def insert_user():
    #insert sql commands go here
    print("you chose insert user")
    a =input("user id#?")
    x =input("user name?")
    y =input("email?")
    c.execute("INSERT INTO user (u_id,u_name,email) VALUES (?, ?, ?)",
          (a,x,y))
    conn.commit()

def insert_subseenit():
    #insert sql commands go here
    os.system('clear')
    a =input("")
    x =input("user name?")
    y =input("email?")
    c.execute("INSERT INTO user (s_id,category,creater_id) VALUES (?, ?, ?)",
          (a,x,y))

def modify():
    #modify sql commands go here
    os.system('clear')
    print("you chose modify")
def delete():
    #delete sql commands go here
    os.system('clear')
    print("you chose delete")
    print("please choose from this table a username")
    display_tables()
    x = input('Enter the value you want to delete: ')
    c.execute("DELETE FROM user WHERE u_name =?", (x,))  #Deletes the row where name = x

    #a test function of our delete
def display_tables():
    #delete sql commands go here
    os.system('clear')
    print("you chose display_tables")
    c.execute('SELECT * FROM user')
    [print (row) for row in c.fetchall()]

build_database()
# loop = True
# while loop:
#     print_menu()

#     selection = input("\n")
#     # for administrator - enter 0 to exit program
#     if selection  == "insert user":
#         insert_user()
#     elif selection  == "delete":
#         delete()
#     elif selection  == "modify":
#         modify()
#     elif selection =="display tables":
#         display_tables()
#     elif selection  == "exit":
#         print ("Thank you, and goodbye!")
#         exit()
#     else:
#        print("we're sorry you entered something not on the menu. Please try again.")
