import sqlite3

def connect():
       conn = sqlite3.connect("faculty.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name VARCHAR, email VARCHAR, \
                     address VARCHAR, mobno VARCHAR,edu VARCHAR, dob VARCHAR, gender VARCHAR)")

       conn.commit()
       conn.close()

def insert(id = " ", name = " ",email = " ", address = " ", mobno = " ", edu = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("faculty.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)", (id, name, email, address , mobno, edu, dob, gender))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("faculty.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM faculty")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("faculty.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM faculty WHERE id = ?", (id,))

       conn.commit()
       conn.close()

def update(id= " ",name = " ", email = " ", address = " ", mobno = " ", edu = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("faculty.db")
       cur = conn.cursor()

       cur.execute("UPDATE faculty SET name = ? OR email = ? OR address = ? OR mobno = ? OR edu = ? OR dob = ? OR gender = ?", \
                   (name, email, address, mobno, edu, dob, gender))

       conn.commit()
       conn.close()

def search(name = " ", email = " ", address = " ", mobno = " ", edu = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("faculty.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM faculty WHERE name = ? OR email = ? OR address = ? OR mobno = ? OR edu = ? OR dob = ? \
                     OR gender = ?", (name, email, address , mobno, edu, dob, gender))
       rows = cur.fetchall()
       return rows
       
       conn.close()

                                                               
connect()
       
