from flask import Flask, request
from TransactionParser import transactionParser

app = Flask(__name__)


@app.route('/addEmployee, methods=["POST"]')
def addEmployee():  # put application's code here
    parser = transactionParser()
    return parser.parse(request.get_json())

if __name__ == '__main__':
    app.run()
