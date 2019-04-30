# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:50:58 2018

@author: Saurabh
"""
import pandas as pd
calpha = """<tbody>
<tr>
<td><span style="text-decoration: underline;"><span style="color: #ff0000;"><strong>Common Name</strong></span></span></td>
<td><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><strong>Tamil</strong></span></span></td>
<td><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><strong>Telugu</strong></span></span></td>
<td><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><strong>Malayalam</strong></span></span></td>
<td><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><strong>Kannada</strong></span></span></td>
<td colspan="2"><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><strong>Hindi</strong></span></span></td>
</tr>
<tr>
<td><span style="color: #000000;">Rice (milled)</span></td>
<td><span style="color: #000000;">Arisi</span></td>
<td><span style="color: #000000;">Biyyam</span></td>
<td><span style="color: #000000;">Ari</span></td>
<td><span style="color: #000000;">Akki</span></td>
<td colspan="2"><span style="color: #000000;">Chaval</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Wheat</span></td>
<td><span style="color: #000000;">Godumai</span></td>
<td><span style="color: #000000;">Godhumalu</span></td>
<td><span style="color: #000000;">Gothmbu</span></td>
<td><span style="color: #000000;">Godhi</span></td>
<td colspan="2"><span style="color: #000000;">Gehun</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Wheat flour</span></td>
<td><span style="color: #000000;">Gothumai maavu</span></td>
<td><span style="color: #000000;">Goduma pindi</span></td>
<td><span style="color: #000000;">Gothambu mavu</span></td>
<td><span style="color: #000000;">Godhi hittu</span></td>
<td colspan="2"><span style="color: #000000;">Atta</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Maize</span></td>
<td><span style="color: #000000;">Makka Cholam</span></td>
<td><span style="color: #000000;">Mokka jonnalu</span></td>
<td><span style="color: #000000;">Cholam</span></td>
<td><span style="color: #000000;">Musikinu jola</span></td>
<td colspan="2"><span style="color: #000000;">Bhutta</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Sorghum</span></td>
<td><span style="color: #000000;">Cholam</span></td>
<td><span style="color: #000000;">Jonnalu</span></td>
<td><span style="color: #000000;">Cholam</span></td>
<td><span style="color: #000000;">Jola</span></td>
<td colspan="2"><span style="color: #000000;">Juar</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Cattail(Pearl) millet</span></td>
<td><span style="color: #000000;">Kambu</span></td>
<td><span style="color: #000000;">Sazzalu</span></td>
<td><span style="color: #000000;">Kambu</span></td>
<td><span style="color: #000000;">Sajje</span></td>
<td colspan="2"><span style="color: #000000;">Bajra</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Foxtail millet</span></td>
<td><span style="color: #000000;">Thenai</span></td>
<td><span style="color: #000000;">Korralu</span></td>
<td><span style="color: #000000;">Thina</span></td>
<td><span style="color: #000000;">Thene</span></td>
<td colspan="2"><span style="color: #000000;">Kangni</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Finger Millet</span></td>
<td><span style="color: #000000;">Kezhvaragu</span></td>
<td><span style="color: #000000;">Ragulu</span></td>
<td><span style="color: #000000;">Moothari</span></td>
<td><span style="color: #000000;">Ragi</span></td>
<td colspan="2"><span style="color: #000000;">Madua</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Samai</span></td>
<td><span style="color: #000000;">Samai</span></td>
<td><span style="color: #000000;">Samai</span></td>
<td><span style="color: #000000;">Chama</span></td>
<td><span style="color: #000000;">Samai</span></td>
<td colspan="2"><span style="color: #000000;">Mutki</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Ladies fingers</span></td>
<td><span style="color: #000000;">Vendakkai</span></td>
<td><span style="color: #000000;">Benda kayi</span></td>
<td><span style="color: #000000;">Vendakka</span></td>
<td><span style="color: #000000;">Bende</span></td>
<td colspan="2"><span style="color: #000000;">Bhindi</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Brinjal</span></td>
<td><span style="color: #000000;">Kathiri</span></td>
<td><span style="color: #000000;">Vankaya</span></td>
<td><span style="color: #000000;">Vazhuthininga</span></td>
<td><span style="color: #000000;">Badane</span></td>
<td colspan="2"><span style="color: #000000;">Baingan</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Papaya</span></td>
<td><span style="color: #000000;">Pappali</span></td>
<td><span style="color: #000000;">Boppayi</span></td>
<td><span style="color: #000000;">Omakaya</span></td>
<td><span style="color: #000000;">Parangi</span></td>
<td colspan="2"><span style="color: #000000;">Papita</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Banana green</span></td>
<td><span style="color: #000000;">Vazhakkai</span></td>
<td><span style="color: #000000;">Arati kayi</span></td>
<td><span style="color: #000000;">Vazhakka</span></td>
<td><span style="color: #000000;">Bale kayi</span></td>
<td colspan="2"><span style="color: #000000;">Kela</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Bengaigram</span></td>
<td><span style="color: #000000;">Kondai kadalai</span></td>
<td><span style="color: #000000;">Sanagalu</span></td>
<td><span style="color: #000000;">Kadala</span></td>
<td><span style="color: #000000;">Kadale</span></td>
<td colspan="2"><span style="color: #000000;">Chenna</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Cowpea</span></td>
<td><span style="color: #000000;">Karamani</span></td>
<td><span style="color: #000000;">Bobbarlu</span></td>
<td><span style="color: #000000;">Payar</span></td>
<td><span style="color: #000000;">Alasande</span></td>
<td colspan="2"><span style="color: #000000;">Lobia</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Indian bean</span></td>
<td><span style="color: #000000;">Mochai</span></td>
<td><span style="color: #000000;">Chikkudu</span></td>
<td><span style="color: #000000;">Avara</span></td>
<td><span style="color: #000000;">Avare</span></td>
<td colspan="2"><span style="color: #000000;">Val</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Broad beans</span></td>
<td><span style="color: #000000;">Avarai</span></td>
<td><span style="color: #000000;">Pedda chikkudu</span></td>
<td><span style="color: #000000;">Avarakka</span></td>
<td><span style="color: #000000;">Chapparadavare</span></td>
<td colspan="2"><span style="color: #000000;">Bakia</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Cluster beans</span></td>
<td><span style="color: #000000;">Kothavarai</span></td>
<td><span style="color: #000000;">Goruchikkudu</span></td>
<td><span style="color: #000000;">Kothavara</span></td>
<td><span style="color: #000000;">Gori kayi</span></td>
<td colspan="2"><span style="color: #000000;">Guar-ki-phalli</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Cucumber</span></td>
<td><span style="color: #000000;">Vellari kai</span></td>
<td><span style="color: #000000;">Dosa kayi</span></td>
<td><span style="color: #000000;">Vellarikka</span></td>
<td><span style="color: #000000;">Souche kayi</span></td>
<td colspan="2"><span style="color: #000000;">Khira</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Greengram</span></td>
<td><span style="color: #000000;">Pasipayir</span></td>
<td><span style="color: #000000;">Pesalu</span></td>
<td><span style="color: #000000;">Cheru Pararu</span></td>
<td><span style="color: #000000;">Hesare kalu</span></td>
<td colspan="2"><span style="color: #000000;">&nbsp;</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Mung</span></td>
<td><span style="color: #000000;">Horsegram</span></td>
<td><span style="color: #000000;">Kollu</span></td>
<td><span style="color: #000000;">Ulavalu</span></td>
<td><span style="color: #000000;">Muthira</span></td>
<td><span style="color: #000000;">Hurule</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Lentil</span></td>
<td><span style="color: #000000;">Kesari paruppu</span></td>
<td><span style="color: #000000;">Misur pappu</span></td>
<td><span style="color: #000000;">Masur parippu</span></td>
<td><span style="color: #000000;">Masur bele</span></td>
<td colspan="2"><span style="color: #000000;">Masur dal</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Peas</span></td>
<td><span style="color: #000000;">Pattani</span></td>
<td><span style="color: #000000;">Batani</span></td>
<td><span style="color: #000000;">Pattani</span></td>
<td><span style="color: #000000;">Batani</span></td>
<td colspan="2"><span style="color: #000000;">Katar</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Redgram</span></td>
<td><span style="color: #000000;">Thuvarai</span></td>
<td><span style="color: #000000;">Kandi</span></td>
<td><span style="color: #000000;">Tuvara</span></td>
<td><span style="color: #000000;">Thugare</span></td>
<td colspan="2"><span style="color: #000000;">Arhar</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Agathi</span></td>
<td><span style="color: #000000;">Agathi</span></td>
<td><span style="color: #000000;">Avise</span></td>
<td><span style="color: #000000;">Agathi</span></td>
<td><span style="color: #000000;">Agase</span></td>
<td colspan="2"><span style="color: #000000;">Agasti</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Cabbage</span></td>
<td><span style="color: #000000;">Muttaikose</span></td>
<td><span style="color: #000000;">Mutta gose</span></td>
<td><span style="color: #000000;">Gos koora</span></td>
<td><span style="color: #000000;">Kosu</span></td>
<td colspan="2"><span style="color: #000000;">Band Gobee</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Coriander leaves</span></td>
<td><span style="color: #000000;">Kothamalli</span></td>
<td><span style="color: #000000;">Kothimiri</span></td>
<td><span style="color: #000000;">Kothamalli</span></td>
<td><span style="color: #000000;">Kothambari Soppu</span></td>
<td colspan="2"><span style="color: #000000;">Hara dhania</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Drumstick</span></td>
<td><span style="color: #000000;">Murungai</span></td>
<td><span style="color: #000000;">Mulaga</span></td>
<td><span style="color: #000000;">Muringa</span></td>
<td><span style="color: #000000;">Nugge</span></td>
<td colspan="2"><span style="color: #000000;">Saijan</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Ash gourd</span></td>
<td><span style="color: #000000;">Poosini kai</span></td>
<td><span style="color: #000000;">Boodida gummadi</span></td>
<td><span style="color: #000000;">Kumbalanga</span></td>
<td><span style="color: #000000;">Budagumbala</span></td>
<td colspan="2"><span style="color: #000000;">Petha</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Bitter gourd</span></td>
<td><span style="color: #000000;">Pavakkai</span></td>
<td><span style="color: #000000;">Kakara kayi</span></td>
<td><span style="color: #000000;">Kaippakka</span></td>
<td><span style="color: #000000;">Hagal kai</span></td>
<td colspan="2"><span style="color: #000000;">Karela</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Bottle gourd</span></td>
<td><span style="color: #000000;">Surai kai</span></td>
<td><span style="color: #000000;">Anapakaya</span></td>
<td><span style="color: #000000;">Charanga</span></td>
<td><span style="color: #000000;">Sorekai</span></td>
<td colspan="2"><span style="color: #000000;">Lowki</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Pumpkin</span></td>
<td><span style="color: #000000;">Parangi kai</span></td>
<td><span style="color: #000000;">Gummadi kayi</span></td>
<td><span style="color: #000000;">Mathan</span></td>
<td><span style="color: #000000;">Kumbala</span></td>
<td colspan="2"><span style="color: #000000;">Kaddu</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Ribbed gourd</span></td>
<td><span style="color: #000000;">Peerkan kai</span></td>
<td><span style="color: #000000;">Beera kayi</span></td>
<td><span style="color: #000000;">Peechinga</span></td>
<td><span style="color: #000000;">Heeraikai</span></td>
<td colspan="2"><span style="color: #000000;">Torai</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Gingelly</span></td>
<td><span style="color: #000000;">Eli</span></td>
<td><span style="color: #000000;">Nuvvuiu</span></td>
<td><span style="color: #000000;">Ellu</span></td>
<td><span style="color: #000000;">Acchsilu</span></td>
<td colspan="2"><span style="color: #000000;">Til</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Sunflower</span></td>
<td><span style="color: #000000;">Surya kanthi</span></td>
<td><span style="color: #000000;">Podduthirugudu puvvu ginzalu</span></td>
<td><span style="color: #000000;">Surya kanthi</span></td>
<td><span style="color: #000000;">surykaamti</span></td>
<td colspan="2"><span style="color: #000000;">Surya mukhi</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Coconut</span></td>
<td><span style="color: #000000;">Thengai</span></td>
<td><span style="color: #000000;">Kobbari</span></td>
<td><span style="color: #000000;">Thenga</span></td>
<td><span style="color: #000000;">Thengini Kai</span></td>
<td colspan="2"><span style="color: #000000;">Nariyal</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Groundnut</span></td>
<td><span style="color: #000000;">Kadalal</span></td>
<td><span style="color: #000000;">Verusanaga</span></td>
<td><span style="color: #000000;">Nilakkadalai</span></td>
<td><span style="color: #000000;">Kadale kayi</span></td>
<td colspan="2"><span style="color: #000000;">Moong phalli</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Mustard</span></td>
<td><span style="color: #000000;">Kadugu</span></td>
<td><span style="color: #000000;">Avalu</span></td>
<td><span style="color: #000000;">Kadugu</span></td>
<td><span style="color: #000000;">Sasuve</span></td>
<td colspan="2"><span style="color: #000000;">Rai</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Chilies</span></td>
<td><span style="color: #000000;">Milagai</span></td>
<td><span style="color: #000000;">Mirapa kaya</span></td>
<td><span style="color: #000000;">Mulaku</span></td>
<td><span style="color: #000000;">Menasina kayi</span></td>
<td colspan="2"><span style="color: #000000;">Mirch</span></td>
</tr>
<tr>
<td><span style="color: #000000;">Turmeric</span></td>
<td><span style="color: #000000;">Manjal</span></td>
<td><span style="color: #000000;">Pasupu</span></td>
<td><span style="color: #000000;">Manjal</span></td>
<td><span style="color: #000000;">Arashina</span></td>
<td colspan="2"><span style="color: #000000;">Haldi</span></td>
</tr>
</tbody>"""

calpha = calpha.split(">")

tchar = '<span style="color: #000000;"'
n=[]
for i in range(len(calpha)):
    if(calpha[i] == tchar):
        n.append(i)

cbeta= []
for i in range(len(n)):
    cbeta.append(calpha[n[i]+1])

for i in range(len(cbeta)):
    cbeta[i] = cbeta[i].split("<")
    cbeta[i] = cbeta[i][0]

c=[]
for i in range(len(cbeta)):
    if(i%6 == 0):
        c.append(cbeta[i])


crop = pd.DataFrame({'col':c})

crop = pd.DataFrame(c)
print(crop)
d = input("Until I fix the bug you'll be 0")
#crop.to_csv('crop.csv')  {to store data into a .csv file format}
