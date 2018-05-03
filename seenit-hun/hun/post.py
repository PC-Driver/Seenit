import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, content, seenit_id, author_id):
    query = "INSERT INTO post (p_id, p_content, seenit_id, author_id) VALUES (" + str(id) + ",'" + content + "'," + str(seenit_id) + "," + str(author_id) + ")"
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("post insert successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("post insert error")

def read_one(id):
    query = "SELECT * FROM post WHERE p_id=" + str(id)
    with conn: 
        try:
            # c.execute(query)
            # items = c.fetchall()
            # item = items[0]
            # print ("post read successfully")
            # return item

            c.execute(query)
            data = c.fetchall()
            formatted_row = '{:<12} {:<60} {:<12} {:<12}'
            print(formatted_row.format("p_id", "p_content", "seenit_id", "author_id"))
            print ("-" * 100)
            for Row in data:
                return formatted_row.format(*Row)
        except:
            print("post read error")        

def delete(s_id):
    query = "DELETE FROM post WHERE p_id={}".format(s_id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("post delete successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("post delete error")


def read_all(seenit_id):
    query = "SELECT * FROM post WHERE seenit_id=" + str(seenit_id)
    # print (query)
    with conn:
        try:
            # c.execute(query)
            # items = c.fetchall()
            # # print (items)
            # print ("post read successfully")
            # return items

            c.execute(query)
            data = c.fetchall()
            formatted_row = '{:<12} {:<60} {:<12} {:<12}'
            print(formatted_row.format("p_id", "p_content", "seenit_id", "author_id"))
            print ("-" * 100)
            for Row in data:
                return formatted_row.format(*Row)
        except:
            print("post read error")

def update(id, content):
    query = "UPDATE post SET p_content='" + content + "' WHERE p_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("post update successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("post update error")

# read_all(1)






