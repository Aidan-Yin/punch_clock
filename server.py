from flask import Flask,render_template,request
import database

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/post',methods=['POST'])
def mainpage_post():
    lastdate = database.getlastdate()
    if not lastdate:
        response = {'lastdate':'2023-02-26'}
        return response
    response = {'lastdate':lastdate}
    return response

@app.route('/upload',methods=['POST'])
def upload():
    date = request.form.get('date')
    content = request.form.get('content')
    database.store(date,content)
    lastdate = database.getlastdate()
    return lastdate

if __name__=='__main__':
    app.run('0.0.0.0',port=8080,debug=False)











