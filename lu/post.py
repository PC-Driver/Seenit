import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, content, seenit_id, author_id):
    query = "INSERT INTO post (p_id, p_content, seenit_id, author_id) VALUES (" + str(id) + ",'" + content + "'," + str(seenit_id) + "," + str(author_id) + ")"
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
    query = "SELECT * FROM post WHERE p_id=" + str(id)
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
    query = "DELETE FROM post WHERE p_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("delete error")

def read_all(seenit_id):
    with conn:
        try:
            c.execute("SELECT * FROM post WHERE seenit_id=" + str(id))
            items = c.fetchall()
            print ("read successfully")
            return items
        except:
            print("read error") 

def update(id, content):
    query = "UPDATE post SET p_content='" + content + "' WHERE p_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("update successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("update error")






