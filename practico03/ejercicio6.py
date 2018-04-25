import pymysql
import json

conn = pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur = conn.cursor()

query = "SELECT * FROM personas"

cur.execute(query)

result = cur.fetchall()

string = json.dumps(result, default=str)

print(string)
