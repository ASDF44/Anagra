

data = """AP—AndhraPradesh,AR—ArunachalPradesh,BR—Bihar,CG—Chhattisgarh,CH—Chandigarh,DD—DamanDiu,DL—Delhi,DN—DadraNagarHaveli,GA—Goa,GJ—Gujarat,HP—HimachalPradesh,HR—Haryana,JH—Jharkhand,JK—JammuKashmir,KA—Karnataka,KL—Kerala,LD—Lakshadweep,MH—Maharashtra,ML—Meghalaya,MN—Manipur,MP—MadhyaPradesh,MZ—Mizoram,NL—Nagaland,OD—Odisha,PB—Punjab,PY—Puducherry,RJ—Rajasthan,SK—Sikkim,TN—TamilNadu,TS—Telangana,TR—Tripura,UP—UttarPradesh,UK—Uttarakhand,WB—WestBengal"""
data_list = data.split(',')
for i in range(len(data_list)):
    data_list[i] = data_list[i].replace('—','')
    data_list[i] = data_list[i].lower()

#print(data_list)
data_dict = {}
for word in data_list:
    data_dict.update({word[2:]: word[0:2]})


print(data_dict)



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sdd"
)

for key in data_dict:
    mycursor = mydb.cursor()

    sql = "UPDATE state_city SET state_code = " + "'" + data_dict[key] + "'"+"where state = " + "'"+key + "';"
    #print(sql)
    mycursor.execute(sql)

    mydb.commit()
