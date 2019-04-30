import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv('C:/Users/Saurabh/SDD/cropdata/apy.csv')
state = str(input("Enter state name : "))
temp_df = df.loc[df['state'] == state]
clist = list(temp_df['crop'])
clist1=[]
for word in clist:
    if word not in clist1:
        clist1.append(word)
print(clist1)

for crop in clist1:
    temp_crop = temp_df.loc[temp_df['crop'] == crop]
   # print(crop,temp_crop['produce'],temp_crop['year'])
    print('\n\n\n')
    plt.title(crop)
    plt.hist(temp_crop['produce']/temp_crop['area'], bins = 20)
    #sns.swarmplot(x=temp_crop['year'], y=temp_crop['produce']/temp_crop['area'])
    plt.xlabel('year')
    plt.ylabel('produce')

    plt.show()


