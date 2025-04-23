from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "Salom"
app.route(debug=True,host="0.0.0.0")