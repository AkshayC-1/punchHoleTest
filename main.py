from flask import request
from flask import jsonify

@app.route("/hello", methods=["GET"])
def get_my_ip():
    print request.remote_addr