
from flask import Flask, jsonify

app = Flask(__name__)
# Well data
wells = [
    {"id": 1, "name": "Well A", "field": "Escravos", "depth_m": 2500},
    {"id": 2, "name": "Well B", "field": "Ughelli", "depth_m": 3200},
    {"id": 3, "name": "Well C", "field": "Forcados", "depth_m": 2800}
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Petroleum Well Data API",
        "status": "running",
        "version": "1.0.0"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
