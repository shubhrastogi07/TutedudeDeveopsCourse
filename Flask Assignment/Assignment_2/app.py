from flask import Flask, request, render_template
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def home():
    current_date = datetime.now()
   
    format = current_date.strftime('%B %d')
    print(format)
    day_of_week = current_date.strftime('%A')
    print(day_of_week)
    time = current_date.strftime('%I:%M %p')
    print(time)
    return render_template('index.html',date=format,dow = day_of_week,time=time)

if __name__== '__main__':
    app.run(debug=True)





