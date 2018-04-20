import pymysql

conector = pymysql.connect(host='localhost', db='tp3', user='root', password='')
cursor = conector.cursor()

sql = 'delete from Persona where idPersona=7'

cursor.execute(sql)
cursor.execute('SELECT * FROM Persona')
select = cursor.fetchall()
print(select)
conector.commit()
conector.close()