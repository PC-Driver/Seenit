import sqlite3 as sql
import logging as f

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, comment_id, author_id):
    query = "INSERT INTO comment_upvote (cu_id, comment_id, author_id) VALUES (" + str(id) + "," + str(comment_id) + "," + str(author_id) + ")"
    # print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("insert comment upvote successfully\n")
            print ("insert successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("insert comment upvote error\n")
            print ("insert error")

def read_one(id):
    query = "SELECT * FROM comment_upvote WHERE cu_id=" + str(id)
    with conn:
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            f.writing("read one comment upvote successfully\n")
            print ("read successfully")
            return item
        except:
            f.writing("read one comment upvote error\n")
            print("read error")

def delete(id):
    query = "DELETE FROM comment_upvote WHERE cu_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("delete comment upvote successfully\n")
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("delete comment upvote error\n")
            print ("delete error")

def read_all(comment_id):
    with conn:
        try:
            c.execute("SELECT * FROM comment_upvote WHERE comment_id=" + str(comment_id))
            items = c.fetchall()
            f.writing("read all comment upvotes successfully\n")
            print ("read successfully")
            return items
        except:
            f.writing("read all comment upvotes error\n")
            print("read error") 