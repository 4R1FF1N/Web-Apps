#Thanks to @JayTech for providing a quick solution - https://stackoverflow.com/questions/22251038/how-to-limit-access-to-flask-for-a-single-ip-address

from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)

trusted_ips = ['127.0.0.1', '192.168.88.136', '192.168.88.139']

@app.route("/", methods=['GET'])
def index():
    return "200 working"

@app.route("/admin", methods=['GET'])
def admin():
    if request.remote_addr not in trusted_ips:
        abort(403)  # Not Found
    else:
        return "1337 admin panel"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)



