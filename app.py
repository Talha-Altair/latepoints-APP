from flask import Flask,render_template, request

app  = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def entry():
    return render_template('index.html')

@app.route('/display',methods=["GET", "POST"])
def display():
    if request.method == "POST":
        sm=int(request.form.get("sm"))
        m=int(request.form.get("m"))
        tl=int(request.form.get("tl"))
        di=int(request.form.get("di"))
        lp=calculate(sm,m,tl,di)
        print(lp) 
    return render_template('result.html', lp=lp)      

"""
def startpy():
    n=int(input("Enter Number of People in Waiting room"))
    if(n>2):
        data()
        calculate()

def data():
    sm=int(input("Enter Number of Senior Managers in Waiting room"))
    m=int(input("Enter Number of People in Waiting room"))
    tl=int(input("Enter Number of People in Waiting room"))
    di=int(input("Enter Number of People in Waiting room"))
"""
def calculate(sm,m,tl,di):
    lp=0
    lp=lp+(sm*8)
    lp=lp+(m*8)
    lp=lp+(tl*8)
    lp=lp+(di*8)
    return lp


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0',port=9500)