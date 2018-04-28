import sqlite3
from classes import User

conn = sqlite3.connect('subseenit.db')
c = conn.cursor()

#drop table if a clean database is required
c.execute("DROP TABLE IF EXISTS user")
c.execute("DROP TABLE IF EXISTS seenit")
c.execute("DROP TABLE IF EXISTS post")
c.execute("DROP TABLE IF EXISTS comment")


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

def insert_user(info):
    with conn:
        c.execute("INSERT INTO user VALUES (:u_id, :u_name, :email)",
                  {'u_id':info.u_id, 'u_name':info.u_name, 'email':info.email})

while True:
    print("-" * 40)
    print ("                Menu")
    print("-" * 40)
    method = input('''   
        1 = Login
        2 = Delete.
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
                a = input("user id#? (choose your favorite number)")
                x = raw_input("user name?")
                y = raw_input("email?")
                new_user = User(a, x, y)
                insert_user(new_user)

            elif login == 2:
                print("2 - Login")
            else:
                break
    else:
        break


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

conn.close()
