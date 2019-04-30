
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='localhost', database='sdd', user='root', password='')
cursor = mydb.cursor()
cursor.execute('select state,city, city_code, lat_long from state_city inner join city_codes on state_city.city = city_codes.city_name')

table_rows = cursor.fetchall()

df = pd.DataFrame(table_rows)

df.columns = ["State", "City", "CC", "LL"]

pivot = df.State.unique()
d = []
for value in pivot:
    d.append(df.loc[df['State'] == value])

mh = {}
    df.loc['']