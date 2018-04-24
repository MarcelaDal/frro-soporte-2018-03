import pymysql

conn = pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur = conn.cursor()
query = "SELECT p.nombre, p.fechaNacimiento, p.dni, p.altura, pp.peso, pp.fecha FROM personas p INNER JOIN personapeso pp on p.id = pp.idPersona "
cur.execute(query)
result = cur.fetchall()

columns = [column[0] for column in cur.description]
for row in result:
    print(dict(zip(columns, row)))
