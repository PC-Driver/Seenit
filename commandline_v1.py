import os
import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def build_database():
    #drop table if a clean database is required
    c.execute("DROP TABLE IF EXISTS user")
    c.execute("DROP TABLE IF EXISTS seenit")
    c.execute("DROP TABLE IF EXISTS post")
    c.execute("DROP TABLE IF EXISTS comment")
    c.execute("DROP TABLE IF EXISTS post_upvote")
    c.execute("DROP TABLE IF EXISTS post_downvote")
    c.execute("DROP TABLE IF EXISTS comment_downvote")
    c.execute("DROP TABLE IF EXISTS comment_upvote")

    c.execute("""CREATE TABLE IF NOT EXISTS user (
                u_id INT NOT NULL,
                u_name VARCHAR(45) NULL,
                email VARCHAR(45) NULL,
                PRIMARY KEY (u_id)
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS seenit(
                s_id INT NOT NULL,
                category VARCHAR(45) NULL,
                creater_id INT NOT NULL,
                PRIMARY KEY (s_id),
                FOREIGN KEY (creater_id)
                REFERENCES user(u_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS post(
                p_id INT NOT NULL,
                p_content VARCHAR(255) NULL,
                seenit_id INT NOT NULL,
                author_id INT NOT NULL,
                created_at DATETIME default CURRENT_TIMESTAMP,
                PRIMARY KEY (p_id),
                FOREIGN KEY (seenit_id)
                REFERENCES seenit (s_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
                FOREIGN KEY (author_id)
                REFERENCES user (u_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS comment(
                c_id INT NOT NULL,
                c_content VARCHAR(255) NULL,
                author_id INT NOT NULL,
                post_id INT NOT NULL,
                created_at DATETIME default CURRENT_TIMESTAMP,
                PRIMARY KEY (c_id),
                FOREIGN KEY (author_id)
                REFERENCES user (u_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
                FOREIGN KEY (post_id)
                REFERENCES post (p_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE            
                )""")
    c.execute("""CREATE TABLE IF NOT EXISTS post_upvote (
                pu_id INT NOT NULL AUTO_INCREMENT,
                author_id INT NOT NULL,
                post_id INT NOT NULL,
                created_at DATETIME default CURRENT_TIMESTAMP,
                PRIMARY KEY (pu_id),
                FOREIGN KEY (author_id)
                REFERENCES user (u_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
                FOREIGN KEY (post_id)
                REFERENCES post (p_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE)""")
    c.execute("""CREATE TABLE IF NOT EXISTS post_downvote (
                pd_id INT NOT NULL AUTO_INCREMENT,
                author_id INT NOT NULL,
                post_id INT NOT NULL,
                created_at DATETIME default CURRENT_TIMESTAMP,
                PRIMARY KEY (pd_id),
                FOREIGN KEY (author_id)
                REFERENCES user (u_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
                FOREIGN KEY (post_id)
                REFERENCES post (p_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE)""") 
    c.execute("""CREATE TABLE IF NOT EXISTS comment_downvote (
            cd_id INT NOT NULL AUTO_INCREMENT,
            author_id INT NOT NULL,
            comment_id INT NOT NULL,
            created_at DATETIME default CURRENT_TIMESTAMP,
            PRIMARY KEY (cd_id),
            FOREIGN KEY (author_id)
            REFERENCES user (u_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
            FOREIGN KEY (comment_id)
            REFERENCES comment (c_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE)""")
    c.execute("""CREATE TABLE IF NOT EXISTS comment_upvote (
                cu_id INT NOT NULL AUTO_INCREMENT,
                author_id INT NOT NULL,
                comment_id INT NOT NULL,
                created_at DATETIME default CURRENT_TIMESTAMP,
                PRIMARY KEY (cu_id),
                FOREIGN KEY (author_id)
                REFERENCES user (u_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
                FOREIGN KEY (comment_id)
                REFERENCES comment (c_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE)""")
    
    
              




def insert_user(info):
    with conn:
        c.execute("INSERT INTO user VALUES (:u_id, :u_name, :email)",
                  {'u_id':info.u_id, 'u_name':info.u_name, 'email':info.email})



with conn: c.execute('INSERT INTO user (u_id, u_name, email) VALUES(1,"Andy","andy@gmail.com")')
with conn: c.execute('INSERT INTO user (u_id, u_name, email) VALUES(2,"Bob","bob@sjsu.edu")')
with conn: c.execute('INSERT INTO user (u_id, u_name, email) VALUES(3,"Chris","chris@yahoo.com")')
with conn: c.execute('INSERT INTO user (u_id, u_name, email) VALUES(4,"Evan","evan@gmail.com")')

with conn: c.execute('INSERT INTO seenit (s_id, category, creater_id) VALUES(1,"news", 2)')
with conn: c.execute('INSERT INTO seenit (s_id, category, creater_id) VALUES(2,"gaming", 4)')
with conn: c.execute('INSERT INTO seenit (s_id, category, creater_id) VALUES(3,"funny", 1)')
with conn: c.execute('INSERT INTO seenit (s_id, category, creater_id) VALUES(4,"pics", 3)')

with conn: c.execute('INSERT INTO comment (c_id, c_content, author_id, post_id) VALUES (1, "Cool", 2, 1)')
with conn: c.execute('INSERT INTO comment (c_id, c_content, author_id, post_id) VALUES (2, "LOL", 3, 4)')

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
loop = True
while loop:
    print_menu()

    selection = input("\n")
    # for administrator - enter 0 to exit program
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
