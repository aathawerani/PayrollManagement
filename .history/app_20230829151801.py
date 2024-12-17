from flask import Flask, request, jsonify
from Transaction import transactionParser

app = Flask(__name__)


@app.route('/addEmployee, methods=["POST"]')
def addEmployee():  # put application's code here
    parser = transactionParser()
    parser.parse(request.json)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
