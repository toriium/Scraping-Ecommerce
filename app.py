from flask import Flask, jsonify
from crawler import laptops_crawler
from datetime import datetime

app = Flask(__name__)


@app.route('/laptops')
def laptops_list():
    result_list_laptops = laptops_crawler()

    actual_datetime = datetime.now()
    full_datetime = actual_datetime.strftime('%d/%m/%Y %H:%M')

    crawler_return = {
        'DateTime': full_datetime,
        'laptops': result_list_laptops
    }
    return jsonify(crawler_return), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
