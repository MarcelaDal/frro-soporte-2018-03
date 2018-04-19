import pymysql

conector = pymysql.connect(host='localhost', db='tp3', user='root', password='')
cursor = conector.cursor()

sql = 'INSERT INTO Persona(nombre ,fecha_nacimiento, dni, altura) VALUES ("tomas","31101996", "39951593", 182)'
cursor.execute(sql)
cursor.execute('SELECT * FROM Persona')
select = cursor.fetchall()
print(select)
conector.commit()