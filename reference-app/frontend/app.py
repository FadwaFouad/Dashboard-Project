from flask import Flask, render_template, request
from flask.json import jsonify

from prometheus_flask_exporter import PrometheusMetrics

from exception import InvalidUsage

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route("/")
def homepage():
    return render_template("main.html")

@app.route("/test")
def test():
    answer = "something"
    return jsonify(repsonse=answer)

@app.route('/error')
def get_error():
    raise InvalidUsage('This view is gone', status_code=410)

@app.route('/error2')
def get_error_2():
    raise InvalidUsage('500 error', status_code=500)

@app.route('/error3')
def get_error_3():
    raise InvalidUsage('502 handle eception', status_code=502)

if __name__ == "__main__":
    app.run()
