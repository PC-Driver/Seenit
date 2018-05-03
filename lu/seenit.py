import sqlite3 as sql
import logging
logging.basicConfig(filename='seenit.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, category, creater_id):
    query = "INSERT INTO seenit (s_id, category, creater_id) VALUES (" + str(id) + ",'" + category + "','" + str(creater_id) + "')"
    with conn:
        try:
            c.execute(query)
            logging.info("insert seenit successfully\n")
            print ("seenit insert successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("insert seenit error\n")
            print ("seenit insert error")

def read_one(id):
    query = "SELECT * FROM seenit WHERE s_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            logging.info("read one seenit successfully\n")
            print ("seenit read successfully")
            return item
        except:
            logging.info("read one seenit error\n")
            print("seenit read error")

def delete(id):
    query = "DELETE FROM seenit WHERE s_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            logging.info("delete seenit successfully\n")
            print ("seenit delete successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("delete seenit error\n")
            print ("seenit delete error")

def read_all():
    with conn:
        try:
            c.execute('SELECT * FROM seenit')
            items = c.fetchall()
            logging.info("read all seenits successfully\n")
            print ("seenit read successfully")
            return items
        except:
            logging.info("read all seenits error\n")
            print("seenit read error")

def update(id, category):
    query = "UPDATE seenit SET category='" + category + "' WHERE s_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            logging.info("update seenit successfully\n")
            print ("seenit update successfully")
            conn.commit()
        except:
            conn.rollback()
            logging.info("update seenit error\n")
            print ("seenit update error")





