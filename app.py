from flask import Flask,render_template,request,redirect,url_for



app=Flask(__name__)


@app.route('/')
def welcome():
    return 'welcome to our House'
@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':

        return render_template('cal_form.html')

    else:
        maths=float(request.form['math_score'])
        eng=float(request.form['english_score'])
        sci=float(request.form['science_score'])
        pro=float(request.form['programing_score'])

        average_score=(maths+eng+sci+pro)/4

        return render_template('cal_form.html',score=average_score)

if __name__=="__main__":
    app.run(debug=True)