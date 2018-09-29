from flask import Flask, request
app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def get_my_ip():
    return request.remote_addr


if __name__ == "__main__":
    app.run()
