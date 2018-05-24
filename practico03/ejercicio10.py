import pymysql

conn = pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur = conn.cursor()
query = "SELECT p.nombre, p.fecha_nacimiento, p.dni, p.altura, pp.peso, pp.fecha FROM persona p INNER JOIN personapeso pp on p.idPersona = pp.idPersona "
cur.execute(query)
result = cur.fetchall()

print(result)

assert result == (('Juan Mannuel', datetime.date(2018, 5, 17), '12345678', 175, 80, datetime.date(2018, 5, 17)),)
