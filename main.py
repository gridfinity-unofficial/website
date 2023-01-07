from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return open("static/index.html").read()


@app.route("/catalog", methods=["GET"])
def catalog():
    return open("static/catalog.html").read()


@app.route("/api/v1/model", methods=["GET", "POST"])
def api_model():
    if request.method == "GET":
        return Response(open("data.json").read(), status=200, mimetype="application/json")
    elif request.method == "POST":
        return Response('{"errors": [{"code": 403, "msg": "making model suggestions is not implemented yet"}]}', status=403, mimetype="application/json")
    elif not request.method == "POST" or not request.method == "GET":
        return Response('{"errors": [{"code": 501, "msg": "not POST and not GET are no allowed methods"}]}', status=501, mimetype="application/json")
    else:
        return Response('{"errors": [{"code": 500, "msg": "an internal server error occurred"}]}', status=500, mimetype="application/json")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
