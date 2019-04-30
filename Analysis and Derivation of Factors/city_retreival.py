import bs4
import requests
import numpy as np
import pandas as pd
cat = {'Delhi':[],
       'AndhraPradesh':[],
       'ArunachalPradesh':[],
       'Assam':[],
       'Bihar':[],
       'Chhattisgarh':[],
       'Goa':[],
       'Gujarat':[],
       'Haryana':[],
       'HimachalPradesh':[],
       'JammuKashmir':[],
       'Jharkhand':[],
       'Karnataka':[],
       'Kerala':[],
       'MadhyaPradesh':[],
       'Maharashtra':[],
       'Manipur':[],
       'Meghalaya':[],
       'Mizoram':[],
       'Nagaland':[],
       'Odisha':[],
       'Punjab':[],
       'Rajasthan':[],
       'Sikkim':[],
       'TamilNadu':[],
       'Telangana':[],
       'Tripura':[],
       'UttarPradesh':[],
       'Uttarakhand':[],
       'WestBengal':[]}



cat =  {key.lower(): value for key, value in cat.items()}


for key in cat:
    #print('https://www.citypopulation.de/php/india-'+char+'.php')
    res = requests.get('https://www.citypopulation.de/php/india-'+key+'.php')
    print(key,' = ',res)
    #print(type(res))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    #print(soup)

    data = ''
    for i in soup.select('span > a'):
        data = data + i.text + ' '
        data_list = data.split(' ')
       # print(key, ' = ',data_list)
    cat[key].extend(data_list)
count = 0
for key in cat:
    for value in cat[key]:
        for i in range(len(value)):
            if value[i] == "'":
                value = ''
                count = count + 1
                break

new_cat = {'state':[], 'city':[]}
for key in cat:
    for value in cat[key]:
        if value != '':
            new_cat['state'].append(key)
            new_cat['city'].append(value)

for i in range(len(new_cat['state'])):
    print(new_cat['state'][i], '  ',new_cat['city'][i] )
#print(max(len(x) for x in new_cat['city']))
#print(new_cat)
print(count)

df = pd.DataFrame(new_cat)
df['city'].replace('', np.nan, inplace=True)
#print(df)
#df.to_csv('C:/Users/Saurabh/SDD/cities list/city_list.csv')
print('done')