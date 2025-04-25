from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("Portfilio.html")

# 404 xato sahifasi uchun handler
@app.errorhandler(404)
def handle_404(error):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
