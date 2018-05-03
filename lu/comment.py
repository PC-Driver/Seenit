import sqlite3 as sql
import logging
logging.basicConfig(filename='seenit.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, content, post_id, author_id):
    query = "INSERT INTO comment (c_id, c_content, post_id, author_id) VALUES (" + str(id) + ",'" + content + "'," + str(post_id) + "," + str(author_id) + ")"
    # print (query)
    with conn:
        try:
            c.execute(query)
            logging.info("Insert comment successfully\n")
            print ("insert successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("Insert comment error\n")
            print ("insert error")

def read_one(id):
    query = "SELECT * FROM comment WHERE c_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            logging.info("read one comment successfully\n")
            print ("read successfully")
            return item
        except:
            logging.info("Read one comment error\n")
            print("read error")

def delete(id):
    query = "DELETE FROM comment WHERE c_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            logging.info("delete comment successfully\n")
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("delete comment error\n")
            print ("delete error")

def read_all(post_id):
    with conn:
        try:
            c.execute("SELECT * FROM comment WHERE post_id=" + str(post_id))
            items = c.fetchall()
            logging.info("read all comments successfully\n")
            print ("read successfully")
            return items
        except:
            logging.info("read all comments error\n")
            print("read error")

def update(id, content):
    query = "UPDATE comment SET c_content='" + content + "' WHERE c_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            logging.info("update comment sucessfully\n")
            print ("update successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("update comment error\n")
            print ("update error")






