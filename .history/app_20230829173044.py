import sys
from flask import Flask, request
from TransactionParser import transactionParser

app = Flask(__name__)

@app.route('/hello')
def hello():  # put application's code here
    return  'Hello World!'

@app.route('/addEmployee, methods=["POST"]')
def addEmployee():  # put application's code here
    print("got here 1", file=sys.stdout)
    parser = transactionParser()
    print("got here 2")
    return parser.parse(request.get_json())

if __name__ == '__main__':
    app.run()
