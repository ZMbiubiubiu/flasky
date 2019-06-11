from flask import Flask


# __author__ == "ZzLee"


app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello'


app.run(host='0.0.0.0', debug=True)
