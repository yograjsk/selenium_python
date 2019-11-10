import sqlite3

conn = sqlite3.connect('mydb.db')

conn.execute("create table student
             (rollNum int not null,
              name text not null,
              age int);")
