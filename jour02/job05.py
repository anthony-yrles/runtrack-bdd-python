import mysql.connector

mydb = mysql.connector.connect(
    host="LocalHost",
    user="root",
    password="SKenan30mg/",
    database="laplateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT SUM(SUPERFICIE) FROM etage")
results = cursor.fetchone()[0]

print(f'La superficie de la Plateforme est {results} m²')

cursor.close()
mydb.close()