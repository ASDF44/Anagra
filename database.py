import mysql.connector
def GetData(city_name):
    connection = mysql.connector.connect(host='localhost',
                                         database='sdd',
                                         user='root',
                                         password='')

    sql_select_Query = "select * from city_codes where city_name = " + "'" + city_name + "'"
  #  print(sql_select_Query)
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
#    print("Total number of city codes in the table are = ", cursor.rowcount)
#    print(type(sql_select_Query))
    for row in records:
        return row[2]


def NCBI(filename):
    connection = mysql.connector.connect(host='localhost',
                                         database='sdd',
                                         user='root',
                                         password='')

    sql_select_Query = "select * from crop where city_name = " + "'" + ncbi + "'"
    #  print(sql_select_Query)
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of city codes in the table are = ", cursor.rowcount)
    print(type(sql_select_Query))
    for row in records:
        return row[2]
