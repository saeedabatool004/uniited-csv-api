from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    rows = []
    with open("data.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return jsonify(rows)

if __name__ == "__main__":
    app.run()