f_name = "C:/Users/Saurabh/Desktop/companion.txt"
import pandas as pd
file = open(f_name, 'r')
l0 = ''
for line in file:
        l0 = l0 + file.readline()


l0 = l0.split()
l=[]
for word in l0:
    (x,y) = (word[:word.index('-')],word[word.index('-')+1:])
    l.append([x,y])
print(l)

df = pd.DataFrame(l)
print(df)























crop = {'barley' : ['hordeum vulgare', 'loamy', 6.0, 7.5, 5.0, 27.0, 195, 'H', 'C:/Users/Saurabh/SDD/ncbi/barley', 2],
'oat' : ['avena sativa', 'loamy', 5.0, 6.5, 3.0, 4.0, 160, 'H', 'C:/Users/Saurabh/SDD/ncbi/oat', 1],
'maize' : ['zea mays', 'loamy', 5.8, 6.8, 18.0, 27.0, 80, 'H', 'C:/Users/Saurabh/SDD/ncbi/maize', 1],
'rice' : ['oryza sativa', 'alluvium', 4.5, 5.0, 20.0, 27.0, 135, 'H', 'C:/Users/Saurabh/SDD/ncbi/rice', 1],
'jowar' : ['sorghum bicolor', 'clayey', 6.0, 7.5, 26.0, 33.0, 120, '', 'C:/Users/Saurabh/SDD/ncbi/jowar', 1],
'wheat' : ['tricitum aestivum', 'loamy', 6.0, 7.5, 20.0, 25.0, 150, 'H', 'C:/Users/Saurabh/SDD/ncbi/wheat', 2],
'cucumber' : ['cucumis sativa', 'loamy', 6.0, 7.0, 15.0, 33.0, 60, 'H', 'C:/Users/Saurabh/SDD/ncbi/cucumber', 1],
'eggplant' : ['solanum melongena', 'loamy', 5.5, 6.0, 26.0, 29.0, 120, 'M', 'C:/Users/Saurabh/SDD/ncbi/eggplant', 0],
'soybean' : ['glycine g. max', 'loamy', 6.5, 7.0, 22.22, 26.67, 110, 'H', 'C:/Users/Saurabh/SDD/ncbi/soybean', 1],
'peanut' : ['arachis hypogaea', 'sandy', 5.5, 7.0, 30.0, 40.0, 100, 'L', 'C:/Users/Saurabh/SDD/ncbi/peanut', 1],
'mustard' : ['brassica nigra', 'loamy', 5.5, 6.8, 18.0, 25.0, 120, 'H', 'C:/Users/Saurabh/SDD/ncbi/mustard', 1],
'sunflower' : ['helianthus annuus', 'clayey', 6.5, 8.0, 13.0, 16.0, 90, 'H', 'C:/Users/Saurabh/SDD/ncbi/sunflower', 2]}
import operator
print('++++++++++++++crop+++++++++++++++++\n',crop,'\n\n\n\n')

print('=================x===============\n')

cd = []
for k, v in crop.items():
    c = [k]
    for a in v:
        c.append(a)
    cd.append(c)

cq = sorted(cd, key=itemgetter(0))

print(cq)
exit()












import mysql.connector

con = mysql.connector.connect(host='localhost',
                                     database='sdd',
                                     user='root',
                                     password='')
print('+=========================+')
print('|  CONNECTED TO DATABASE  |')
print('+=========================+')

cur = con.cursor()
cur.execute("SELECT city_name, city_code FROM city_codes"
            "")

data1 = cur.fetchall()


data = {}

for val in data1:
    data[val[0]] = val[1]


print(data)