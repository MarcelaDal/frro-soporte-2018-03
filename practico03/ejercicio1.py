import pymysql


conector = pymysql.connect(host='localhost',db='tp3', user='root', password='')
cursor = conector.cursor()
sql = 'CREATE TABLE IF NOT EXISTS Persona(idPersona integer PRIMARY KEY,nombre char(30),fecha_' \
      'nacimiento Date,dni char(13),altura integer);'
cursor.execute(sql)
sql = 'SELECT * FROM Persona'
cursor.execute(sql)
select = cursor.fetchall()
columnas = [columna[0] for columna in cursor.description]
for fila in select:
    print(dict(zip(columnas, fila)))
conector.commit()
conector.close()




