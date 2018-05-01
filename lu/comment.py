import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, content, post_id, author_id):
    query = "INSERT INTO comment (c_id, c_content, post_id, author_id) VALUES (" + str(id) + ",'" + content + "'," + str(post_id) + "," + str(author_id) + ")"
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
    query = "SELECT * FROM comment WHERE c_id=" + str(id)
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
    query = "DELETE FROM comment WHERE c_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("delete error")

def read_all(post_id):
    with conn:
        try:
            c.execute("SELECT * FROM comment WHERE post_id=" + str(post_id))
            items = c.fetchall()
            print ("read successfully")
            return items
        except:
            print("read error") 

def update(id, content):
    query = "UPDATE comment SET c_content='" + content + "' WHERE c_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("update successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("update error")






