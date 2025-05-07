#import packages
from flask import Flask, render_template, request
from snowFlakeConnection import sfconnect
import pandas as pd

app = Flask("my website")

@app.route('/')
def homepage():
    cur = cnx.cursor().execute("select name,count(*) "
    "from colors "
    "group by name order by count(*) desc")
    # ("SELECT current_account()")
    rows = pd.DataFrame(cur.fetchall(), columns=['Väri', 'lkm'])
    dfhtml = rows.to_html(index=False)  # print(rows)
    # print(dfhtml)
    # onerow = cur.fetchone()
    return render_template('index.html', dfhtml=dfhtml)

@app.route('/submit')
def submitpage():
    return render_template('submit.html')

@app.route('/coolcharts')
def coolit():
    cur = cnx.cursor().execute("select name,count(*) "
    "from colors "
    "group by name order by count(*) desc")
    data4Charts = pd.DataFrame(cur.fetchall(),columns=['color','votes'])
    #data4Charts.to_csv('E:/data4charts.csv', index=False)
    #data4ChartsJSON = data4Charts.to_json("E:/data4ChartsJSON.json", orient='records')
    data4ChartsJSON = data4Charts.to_json(orient='records')

    return render_template('coolcharts.html', data4ChartsJSON=data4ChartsJSON)
@app.route('/thanks4submit', methods=['POST'])
def thanks4submit():
    colorname = request.form.get("cname")
    username = request.form.get("uname")
    cnx.cursor().execute(
        "INSERT INTO COLORS(UID, NAME) " + "SELECT COLOR_UID_SEQ.nextval, '" + colorname + "'")

    return render_template('thanks4submit.html', colorname=colorname, username=username)

#snowflake
cnx=sfconnect()
#cur = cnx.cursor()
app.run()

