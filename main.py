from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "TEST" #Change this to somehting actually secret, Long and random.

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/info')
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
#This will make the website run on all your adapters
#So if you're running this on a VPS, it will expose it to the internet as long as they access it with the correct IP&Port.
#To make it private, change it to localhost