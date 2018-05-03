import sqlite3 as sql
import logging as f

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, content, seenit_id, author_id):
    query = "INSERT INTO post (p_id, p_content, seenit_id, author_id) VALUES (" + str(id) + ",'" + content + "'," + str(seenit_id) + "," + str(author_id) + ")"
    # print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("insert post successfully\n")
            print ("post insert successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("insert post error\n")
            print ("post insert error")

def read_one(id):
    query = "SELECT * FROM post WHERE p_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            f.writing("read one post successfully\n")
            print ("post read successfully")
            return item
        except:
            f.writing("read one post error\n")
            print("post read error")

def delete(s_id):
    query = "DELETE FROM post WHERE p_id={}".format(s_id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("delete post successfully\n")
            print ("post delete successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("delete post error\n")
            print ("post delete error")

def read_all(seenit_id):
    query = "SELECT * FROM post WHERE seenit_id=" + str(seenit_id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            items = c.fetchall()
            # print (items)
            f.writing("read all posts successfully\n")
            print ("post read successfully")
            return items
        except:
            f.writing("read all posts error\n")
            print("post read error")

def update(id, content):
    query = "UPDATE post SET p_content='" + content + "' WHERE p_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("update post successfully\n")
            print ("post update successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("update post error\n")
            print ("post update error")

# read_all(1)