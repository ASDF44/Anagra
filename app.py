from flask import Flask, render_template, request
import weather
import database
import mysql.connector
import datetime
import analysis
print(-1)
app = Flask(__name__)


print(0)

con = mysql.connector.connect(host='localhost',
                                     database='sdd',
                                     user='root',
                                     password='')

print(1)


@app.route('/')
def hello_world():

    cur = con.cursor()
    cur.execute("SELECT city_name, city_code FROM city_codes ORDER BY city_name")
    datax = cur.fetchall()
    data2 = {}
    for val in datax:
        data2[val[0]] = str(val[1])
    print(4)


    cur.execute("SELECT distinct state FROM state_city ORDER BY state ")
    datax = cur.fetchall()
    data1 = [val[0] for val in datax]
    print(5)


    sql_select_Query = "select * from crop ORDER BY Name "
    #  print(sql_select_Query)
    cur = con.cursor()
    cur.execute(sql_select_Query)
    records = cur.fetchall()
    data3 = {}
    for val in records:
        data3[val[0]] = list(val[1:])
    print(6)
    return render_template('select.html', d1 = data1, d2 = data2, d3 = data3)

print(7)


@app.route('/', methods =['POST'])
def submit():
    print(8)
    cur = con.cursor()
    cur.execute("SELECT * FROM crop")
    datax = cur.fetchall()
    data = {}
    data['state'] = request.form['state']
    data['city'] = request.form['city']
    data['soil'] = request.form['soil']
    data['pH'] = request.form['pH']
    data['temp'] = request.form['temp']
    data['pcrop'] = request.form['pcrop']
    data['N'] = request.form['N']
    city_code = data['city']
    wthr = weather.GetWeather(city_code)
    t =[ datetime.datetime.fromtimestamp(wthr['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
         datetime.datetime.fromtimestamp(wthr['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')]

    c1 = request.form['analysis1']
    c2 = request.form['analysis2']
    ci = [c1,c2]
#    print(c1, '', len(c1), '\n\n', c2,'',len(c2), '\n\n')
    sql_select_Query1 = "select ncbi from crop where Name = " + "'" + c1 + "'"
    sql_select_Query2 = "select ncbi from crop where Name = " + "'" + c2 + "'"

    cur = con.cursor()
    cur.execute(sql_select_Query1)
    records1 = cur.fetchall()
    cur.execute(sql_select_Query2)
    records2 = cur.fetchall()
    location = [records1[0][0]+'.txt', records2[0][0]+'.txt']
#    print("=================records are=================\n",location)
    seq = [analysis.GetNCBI(location[0]), analysis.GetNCBI(location[1])]
#    print(seq)
    alignment = analysis.align(seq[0], seq[1])
#    print(alignment)
    score = round(analysis.align_score(alignment),2)
#    print(score)


    sql_select_Query = "select * from crop"
    cur = con.cursor()
    cur.execute(sql_select_Query)
    rec = cur.fetchall()
    cd = []
    for val in rec:
        cd.append([v for v in val])


#    print(crop_data)

    for v in cd:
        crop_score = 0
        if float(data['temp']) > v[5] and float(data['temp']) < v[6]:
            crop_score += 1.35532

        if float(data['pH']) > v[3] and float(data['pH']) < v[4]:
            crop_score += 3.56787

        if data['N'] == v[8]:
            crop_score += 4.99675
        v.append(crop_score)

    for i in range(len(cd)):
        for j in range(i,len(cd)):
            if cd[i][-1] < cd[j][-1]:
                temp = cd[i]
                cd[i] = cd[j]
                cd[j] = temp

    print('\n\n')
    for i in range(len(cd)):
        print('****************************',cd[i][0],'  ',cd[i][-1])

    return render_template('weather.html',ci = ci, d = data, c = city_code, w = wthr, t = t, l = location, s = score, a = alignment, seq = seq, cd = cd)


#app.secret_key = "ljbskjbd%$#()@*;.kmsj"

@app.route('/crop_analysis')
def crop_analysis():
    return render_template('crop_analysis.html')



@app.route('/crop_bio_analysis')
def bio():
    return render_template('bio_analysis.html')


if __name__ == '__main__':
    app.run(debug=True)
