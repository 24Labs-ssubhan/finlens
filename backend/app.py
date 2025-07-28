from flask import Flask, request, jsonify
from categoriser import categorise_transactions
from summary import generate_summary

app = Flask(__name__)

@app.route('/api/categorise', methods=['POST'])
def categorise():
    data = request.get_json()
    result = categorise_transactions(data)
    return jsonify(result)

@app.route('/api/summary', methods=['POST'])
def summary():
    data = request.get_json()
    result = generate_summary(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
