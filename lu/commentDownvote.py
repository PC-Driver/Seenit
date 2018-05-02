import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, comment_id, author_id):
    query = "INSERT INTO comment_downvote (cd_id, comment_id, author_id) VALUES (" + str(id) + "," + str(comment_id) + "," + str(author_id) + ")"
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("insert successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("insert error")

def read_one(id):
    query = "SELECT * FROM comment_downvote WHERE cd_id=" + str(id)
    with conn: 
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            print ("read successfully")
            return item 
        except:
            print("read error")        

def delete(id):
    query = "DELETE FROM comment_downvote WHERE cd_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("delete error")

def read_all(comment_id):
    with conn:
        try:
            c.execute("SELECT * FROM comment_downvote WHERE comment_id=" + str(comment_id))
            items = c.fetchall()
            print ("read successfully")
            return items
        except:
            print("read error") 







