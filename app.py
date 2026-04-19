from flask import Flask, jsonify
import csv
import os

app = Flask(__name__)

@app.route("/api/data", methods=["GET"])
def get_data():
    rows = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "data.csv")
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return jsonify(rows)