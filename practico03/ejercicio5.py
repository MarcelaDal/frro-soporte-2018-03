import pymysql

conector = pymysql.connect(host='localhost', db='tp3', user='root', password='')
cursor = conector.cursor()

sql='UPDATE `Persona` SET `nombre`="Marcela",`fecha_nacimiento`="2/6/95",`dni`="38770609",`altura`=182 WHERE idPersona=2'
cursor.execute(sql)
cursor.execute('SELECT * FROM Persona WHERE idPersona=2')
select = cursor.fetchall()
print(select)
conector.commit()