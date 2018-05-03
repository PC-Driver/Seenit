import sqlite3 as sql
import logging as f

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, post_id, author_id):
    query = "INSERT INTO post_upvote (pu_id, post_id, author_id) VALUES (" + str(id) + "," + str(post_id) + "," + str(author_id) + ")"
    # print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("insert post upvote successfully\n")
            print ("insert successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("insert post upvote error\n")
            print ("insert error")

def read_one(id):
    query = "SELECT * FROM post_upvote WHERE pu_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            f.writing("read one post upvote successfully\n")
            print ("read successfully")
            return item
        except:
            f.writing("read one post upvote error\n")
            print("read error")

def delete(id):
    query = "DELETE FROM post_upvote WHERE pu_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("delete post upvote successfully\n")
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("delete post upvote error\n")
            print ("delete error")

def read_all(post_id):
    with conn:
        try:
            c.execute("SELECT * FROM post_upvote WHERE post_id=" + str(post_id))
            items = c.fetchall()
            f.writing("read all post upvote successfully\n")
            print ("read successfully")
            return items
        except:
            f.writing("read all post upvote error\n")
            print("read error")


read_all(1)