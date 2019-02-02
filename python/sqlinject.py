import pymysql

db = pymysql.connect(host="localhost",
user="",
passwd="",
db="")

cur = db.cursor()

platform = input('Enter language: ')

cur.execute(query="SELECT * FROM platforms WHERE language = %s;", args=(platform,))
for row in cur.fetchall():
    print(row)

db.close()