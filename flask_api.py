from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/app/esg_rating', methods=['GET'])
def esg_rating():
    response = {
        "data": {
            "esg_rating": 4
        },
        "status": 200
    }
    return jsonify(response)

@app.route('/app/cmpr_data', methods=['GET'])
def comparison_chart():
    response = {
        "data": {
            "labels": ["Company 1", "Company 2", "Company 3", "Company 4", "Company 5"],
            "data": [10, 20, 30, 40, 50]
        },
        "status": 200
    }
    return jsonify(response)

@app.route('/app/frqncy_data', methods=['GET'])
def keyword_frequency_chart():
    response = {
        "data": {
            "keywords": ["keyword1", "keyword2", "keyword3"],
            "frequency_counts": [70, 20, 35]
        },
        "status": 200
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
