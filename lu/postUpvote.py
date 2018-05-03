import sqlite3 as sql
import logging
logging.basicConfig(filename='seenit.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, post_id, author_id):
    query = "INSERT INTO post_upvote (pu_id, post_id, author_id) VALUES (" + str(id) + "," + str(post_id) + "," + str(author_id) + ")"
    with conn:
        try:
            c.execute(query)
            logging.info("insert post upvote successfully\n")
            print ("insert successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("insert post upvote error\n")
            print ("insert error")

def read_one(id):
    query = "SELECT * FROM post_upvote WHERE pu_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            logging.info("read one post upvote successfully\n")
            print ("read successfully")
            return item
        except:
            logging.info("read one post upvote error\n")
            print("read error")

def delete(id):
    query = "DELETE FROM post_upvote WHERE pu_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            logging.info("delete post upvote successfully\n")
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("delete post upvote error\n")
            print ("delete error")

def read_all(post_id):
    with conn:
        try:
            c.execute("SELECT * FROM post_upvote WHERE post_id=" + str(post_id))
            items = c.fetchall()
            logging.info("read all post upvote successfully\n")
            print ("read successfully")
            return items
        except:
            logging.info("read all post upvote error\n")
            print("read error")





