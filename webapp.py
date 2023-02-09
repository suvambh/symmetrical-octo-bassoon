from flask import Flask, render_template, request
from exchange_calc import rate_calc

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def home_post():
    print("Post")
    source_value = request.form['source']
    destination_value = request.form['destination']
    rate = rate_calc(source_value, destination_value)
    #rate = source_value+destination_value
    print("Rate is ", rate)
    return render_template("index.html", output=rate,
                           source_value=source_value, destination_value=destination_value)

app.run()




