import sqlite3

conn = sqlite3.connect('mydb.db')

# conn.execute("create table student (rollNum int not null, name text not null, age int);")

# conn.execute("delete from student where rollNum=12")
conn.execute("insert into student (rollNum, name, age) values(?, ?, ?)", (15, 'Mahesh', 30))
conn.commit()


data = conn.execute("select * from student")
print(data)
print(type(data))
for i in data:
    print("rollNum: ", i[0])
    print("name: ", i[1])
    print("age: ", i[2])

