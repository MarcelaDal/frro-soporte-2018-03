import pymysql
import datetime
import json

conn = pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur = conn.cursor()

query = "SELECT * FROM persona"

cur.execute(query)

result = cur.fetchall()

#string = json.dumps(result, default=str)


assert result == ((0, 'Juan Mannuel', datetime.date(2018, 5, 17), '12345678', 175),)
