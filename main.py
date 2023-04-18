from flask import Flask, Response, request
from os import listdir

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return open("static/index.html").read()


@app.route("/catalog", methods=["GET"])
def catalog():
    return open("static/catalog.html").read()


@app.route("/specifications", methods=["GET"])
def specifications():
    return open("static/specifications.html").read()


@app.route("/faq", methods=["GET"])
def faq():
    return open("static/faq.html").read()


@app.route("/api/v1/faq", methods=["GET", "POST"])
def api_faq():
    if request.method == "GET":
        return Response(open("data/faq.json").read(), status=200, mimetype="application/json")
    elif request.method == "POST":
        return Response('{"errors": [{"code": 403, "msg": "asking questions is not implemented yet"}]}', status=403, mimetype="application/json")
    elif not request.method == "POST" or not request.method == "GET":
        return Response('{"errors": [{"code": 501, "msg": "not POST and not GET are no allowed methods"}]}', status=501, mimetype="application/json")
    else:
        return Response('{"errors": [{"code": 500, "msg": "an internal server error occurred"}]}', status=500, mimetype="application/json")


@app.route("/api/v1/model", methods=["GET", "POST"])
def api_model():
    if request.method == "GET":
        return Response(open("data/model.json").read(), status=200, mimetype="application/json")
    elif request.method == "POST":
        return Response('{"errors": [{"code": 403, "msg": "making model suggestions is not implemented yet"}]}', status=403, mimetype="application/json")
    elif not request.method == "POST" or not request.method == "GET":
        return Response('{"errors": [{"code": 501, "msg": "not POST and not GET are no allowed methods"}]}', status=501, mimetype="application/json")
    else:
        return Response('{"errors": [{"code": 500, "msg": "an internal server error occurred"}]}', status=500, mimetype="application/json")


@app.route("/scripts/<script>", methods=["GET"])
def scripts(script):
    if script == "theme":
        return Response(open("static/scripts/theme.js"), status=200, mimetype="text/javascript")
    else:
        return Response(str({"errors": [{"code": 404, "msg": f"{script} is no valid script"}]}), status=404, mimetype="application/json")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
