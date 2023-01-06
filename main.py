from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return open("static/index.html").read()


@app.route("/api/v1/model", methods=["GET", "POST"])
def api_model():
    pass


@app.route("/api/v1/model/<model_id>", methods=["PUT", "DELETE"])
def api_model_id(model_id: str):
    print(model_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
