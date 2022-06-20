
from flask import Flask, render_template
from datetime import datetime, timedelta
#get current time in your local timezone
current_time=datetime.now()
n=1
#I used timedelta to substract 1 hour
past_time=current_time-timedelta(hours=n)

app=Flask(__name__)


@app.route("/")
def home():
    current_time=datetime.now()
    
    return render_template("index.html"  , content1=current_time)
   


@app.route("/past" , methods=['POST','GET'])
def result():
    current_time=datetime.now()
    past_time=current_time-timedelta(hours=n)

    return render_template("index.html"  ,content2=past_time)
    
