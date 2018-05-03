# run this file to create the database and tables before running the app
import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def create_tables():
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
                u_name VARCHAR(45) NULL UNIQUE,
                pwd VARCHAR(45) NULL,
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
                p_content VARCHAR(45) NULL,
                seenit_id INT NOT NULL,
                author_id INT NOT NULL,
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
                pu_id INT NOT NULL,
                author_id INT NOT NULL,
                post_id INT NOT NULL,
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
                pd_id INT NOT NULL,
                author_id INT NOT NULL,
                post_id INT NOT NULL,
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
            cd_id INT NOT NULL,
            author_id INT NOT NULL,
            comment_id INT NOT NULL,
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
                cu_id INT NOT NULL,
                author_id INT NOT NULL,
                comment_id INT NOT NULL,
                PRIMARY KEY (cu_id),
                FOREIGN KEY (author_id)
                REFERENCES user (u_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
                FOREIGN KEY (comment_id)
                REFERENCES comment (c_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE)""")

def insert_users():
    with conn: 
        c.execute('INSERT INTO user (u_id, u_name, email) VALUES(1,"Andy","andy@gmail.com")')
        c.execute('INSERT INTO user (u_id, u_name, email) VALUES(2,"Bob","bob@sjsu.edu")')
        c.execute('INSERT INTO user (u_id, u_name, email) VALUES(3,"Chris","chris@yahoo.com")')
        c.execute('INSERT INTO user (u_id, u_name, email) VALUES(4,"Evan","evan@gmail.com")')

def insert_seenits():
    with conn: 
        try:
            c.execute('INSERT INTO seenit (s_id, category, creater_id) VALUES(1,"news", 2)')
            c.execute('INSERT INTO seenit (s_id, category, creater_id) VALUES(2,"gaming", 4)')
            c.execute('INSERT INTO seenit (s_id, category, creater_id) VALUES(3,"funny", 1)')
            c.execute('INSERT INTO seenit (s_id, category, creater_id) VALUES(4,"pics", 3)')
            # print ("done inserting seents")
        except:
            print ("error inserting seenits")

def insert_posts():
    with conn:
        c.execute('INSERT INTO post VALUES (1,"Beautiful sunset reflecting on the sea.",4,2)')
        c.execute('INSERT INTO post VALUES (2,"Animal shelters across U.S. teach cats how to high five to make them more attractive for adoption",1,3)')
        c.execute('INSERT INTO post VALUES (3,"This is how my fathers dog says hello to me when I go to see him",3,4)')
        c.execute('INSERT INTO post VALUES (4,"Is this the game that everyone is talking about [OC]",2,1)')

def insert_comments():
    with conn:
        c.execute('INSERT INTO comment VALUES (1,"cool",2,1)')
        c.execute('INSERT INTO comment VALUES (2,"LOL",3,3)')
        c.execute('INSERT INTO comment VALUES (3,"beautiful",4,1)')
        c.execute('INSERT INTO comment VALUES (4,"funny",3,2)')

def insert_post_upvote():
    with conn:
        c.execute('INSERT INTO post_upvote VALUES (1,1,1)')
        c.execute('INSERT INTO post_upvote VALUES (2,2,2)')
        c.execute('INSERT INTO post_upvote VALUES (3,3,3)')
        c.execute('INSERT INTO post_upvote VALUES (4,4,4)')
        c.execute('INSERT INTO post_upvote VALUES (5,1,2)')
        c.execute('INSERT INTO post_upvote VALUES (6,1,3)')
        c.execute('INSERT INTO post_upvote VALUES (7,1,4)')

def show_users():
    with conn:
        c.execute('SELECT * FROM user')
        users = c.fetchall()
        print (users)

def show_seenits():
    with conn:
        c.execute('SELECT * FROM seenit')
        seenits = c.fetchall()
        # for s in seenits:
        #     print (s)
        print (seenits)

def show_posts():
    with conn:
        c.execute('SELECT * FROM post')
        posts = c.fetchall()
        print (posts)

def show_comments():
    with conn:
        c.execute('SELECT * FROM comment')
        comments = c.fetchall()
        print (comments)

def show_post_upvotes():
    with conn:
        c.execute('SELECT * FROM post_upvote')
        pus = c.fetchall()
        print (pus)

# create_tables()
# insert_users()
# insert_seenits()
# insert_posts()
# insert_comments()
# insert_post_upvote()
# show_seenits()
# show_posts()
# show_comments()
# show_post_upvotes()
