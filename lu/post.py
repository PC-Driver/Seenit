import sqlite3 as sql
import logging
logging.basicConfig(filename='seenit.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
                    
conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, content, seenit_id, author_id):
    query = "INSERT INTO post (p_id, p_content, seenit_id, author_id) VALUES (" + str(id) + ",'" + content + "'," + str(seenit_id) + "," + str(author_id) + ")"
    with conn:
        try:
            c.execute(query)
            logging.info("insert post successfully\n")
            print ("post insert successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("insert post error\n")
            print ("post insert error")

def read_one(id):
    query = "SELECT * FROM post WHERE p_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            logging.info("read one post successfully\n")
            print ("post read successfully")
            return item
        except:
            logging.info("read one post error\n")
            print("post read error")

def delete(p_id):
    query = "DELETE FROM post WHERE p_id={}".format(p_id)
    with conn:
        try:
            c.execute(query)
            logging.info("delete post successfully\n")
            print ("post delete successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("delete post error\n")
            print ("post delete error")

def read_all(seenit_id):
    query = "SELECT * FROM post WHERE seenit_id=" + str(seenit_id)
    with conn:
        try:
            c.execute(query)
            items = c.fetchall()
            logging.info("read all posts successfully\n")
            print ("post read successfully")
            return items
        except:
            logging.info("read all posts error\n")
            print("post read error")

def update(id, content):
    query = "UPDATE post SET p_content='" + content + "' WHERE p_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            logging.info("update post successfully\n")
            print ("post update successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("update post error\n")
            print ("post update error")







