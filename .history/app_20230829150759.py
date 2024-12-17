from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/addEmployee, methods=["POST"]')
def addEmployee():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
