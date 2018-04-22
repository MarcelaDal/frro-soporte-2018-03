import pymysql
import datetime

conn = pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur = conn.cursor()
inputId = input("Ingrese el id de la persona: ")
query = "SELECT p.id, max(pp.fecha), p.nombre FROM personas p LEFT JOIN personapeso pp on p.id = pp.idPersona WHERE p.id = %s"
cur.execute(query, [inputId])
result = cur.fetchone()

dateToday= datetime.date.today()

if result[0]:
    if result[1] == None or str(result[1]) < str(dateToday):
        inputPeso = float(input("Ingrese el peso para "+result[2]+" : "))
        query2 = "INSERT INTO personapeso values (%s, %s, %s, %s)"
        cur.execute(query2, [0, result[0], 60, dateToday])
        conn.commit()
        print("Registro agregado exitosamente.")
    else:
        print("Ya existe un registro para el peso de "+result[2]+" que es menor o igual a la fecha especificada.")
else:
    print("No existe ninguna persona con id 2")


