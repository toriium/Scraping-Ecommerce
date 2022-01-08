from flask import Flask, jsonify
from crawler import laptops_crawler
from datetime import datetime
from operator import itemgetter

app = Flask(__name__)


@app.route('/laptops')
def laptops_list():
    result_laptops_list = laptops_crawler()

    ordained_laptops_list = sorted(result_laptops_list, key=itemgetter('price_hdd_128'))

    actual_datetime = datetime.now()
    full_datetime = actual_datetime.strftime('%d/%m/%Y %H:%M')

    crawler_return = {
        'DateTime': full_datetime,
        'laptops': ordained_laptops_list
    }
    return jsonify(crawler_return), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
