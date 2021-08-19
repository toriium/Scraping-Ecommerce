from flask import Flask, jsonify
from crawler import laptops_crawler

app = Flask(__name__)


@app.route('/laptops')
def laptops_list():
    result = jsonify(laptops_crawler())
    return result,200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
