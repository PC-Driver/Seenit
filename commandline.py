import os
import sqlite3
#galatians 6:9
conn = sqlite3.connect('subseenit.db')
c = conn.cursor

def print_menu():
        #MENU DESIGN!
        print (33* "-", "MENU" , 33 * "-")
        print( "|", 30 * " ", "insert user", 30 * " ", "|", )
        print( "|", 30 * " ", "insert subseenit", 30 * " ", "|", )
        print( "|", 30 * " ", "modify", 30 * " ", "|", )
        print( "|", 30 * " ", "delete", 30 * " ", "|", )
        print( "|", 30 * " ", "display tables", 22 * " ", "|", )
        print( "|", 30 * " ", "exit", 32 * " ", "|", )
        print (72* "-")

def insert_user():
    #insert sql commands go here
    print("you chose insert user")
    a =input("user id#? (choose your favorite number)")
    x =input("user name?")
    y =input("email?")
    c.execute("INSERT INTO user (a,x,y) VALUES (?, ?, ?)",
          (a,x,y))
    conn.commit()

def insert_subseenit():
    #insert sql commands go here
    os.system('clear')

    
def modify():
    #modify sql commands go here
    os.system('clear')
    print("you chose modify")
def delete():
    #delete sql commands go here
    os.system('clear')
    print("you chose delete")
def display_tables():
    #delete sql commands go here
    os.system('clear')
    print("you chose display_tables")


loop = True
while True:
    print_menu()
   
    selection = input("\n") #for administrator - enter 0 to exit program
    if selection  == "insert user":
        insert_user()
    elif selection  == "delete":
        delete()
    elif selection  == "modify":
        modify()
    elif selection =="display tables":
        display_tables()
    elif selection  == "exit":
        print ("Thank you, and goodbye!")
        exit()
    else:
       print("we're sorry you entered something not on the menu. Please try again.")
 
