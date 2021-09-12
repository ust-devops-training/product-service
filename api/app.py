from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/api/1.0/products/", methods=['GET'])
def get_products():
    products = [
        {
            'id': 1,
            'name': '.NET Design Patterns',
            'CategoryID': 101
         },
        {
            'id': 2,
            'name': 'Pen Drive',
            'CategoryID': 102
        },
        {
            'id': 3,
            'name': 'Pepsi 300 ML',
            'CategoryID': 103
        }
    ]
    return jsonify({'Products': products})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=False)
