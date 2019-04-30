import mysql.connector

mydb = mysql.connector.connect(host="localhost",database="sdd",user="root",password="")

sql_select_Query = "select distinct(state) from state_city "
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

city=[row[0] for row in records]


for value in city:
    mycursor = mydb.cursor()
    sql = "CREATE TABLE "+ value+ " (city_name varchar(50), city_id int(9), lat_long varchar(50))"
    print(sql)
    mycursor.execute(sql)
mydb.commit()
print("DONE")
