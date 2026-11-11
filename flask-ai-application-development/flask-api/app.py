from flask import Flask, jsonify, request

import requests

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

@app.route("/api/wells", methods=["GET"])
def get_wells():
    return jsonify(wells), 200


@app.route("/api/wells/<int:well_id>", methods=["GET"])
def get_well(well_id):

    well = next(
        (w for w in wells if w["id"] == well_id),
        None
    )

    if well is None:
        return jsonify({"error": "Well not found"}), 404

    return jsonify(well), 200



@app.route("/api/wells", methods=["POST"])
def create_well():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Valid JSON object required"}), 400

    required_fields = ["name", "field", "depth_m"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    if not all(isinstance(data[f], str) and data[f].strip()
               for f in ["name", "field"]):
        return jsonify({"error": "Name and field must be non-empty strings"}), 400

    if (isinstance(data["depth_m"], bool)
            or not isinstance(data["depth_m"], (int, float))
            or data["depth_m"] <= 0):
        return jsonify({"error": "Depth must be a positive number"}), 400

    new_well = {
        "id": max(w["id"] for w in wells) + 1,
        "name": data["name"],
        "field": data["field"],
        "depth_m": data["depth_m"]
    }

    wells.append(new_well)

    return jsonify(new_well), 201

@app.route("/api/wells/<int:well_id>", methods=["PUT"])
def update_well(well_id):

    well = next((w for w in wells if w["id"] == well_id), None)

    if well is None:
        return jsonify({"error": "Well not found"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Valid JSON required"}), 400

    if not all(k in data for k in ["name", "field", "depth_m"]):
        return jsonify({"error": "All fields are required"}), 400

    well.update({
        "name": data["name"],
        "field": data["field"],
        "depth_m": data["depth_m"]
    })

    return jsonify(well), 200

@app.route("/api/wells/<int:well_id>", methods=["PATCH"])
def patch_well(well_id):

    well = next((w for w in wells if w["id"] == well_id), None)

    if well is None:
        return jsonify({"error": "Well not found"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data:
        return jsonify({"error": "Valid non-empty JSON required"}), 400

    if not set(data).issubset({"name", "field", "depth_m"}):
        return jsonify({"error": "Invalid fields supplied"}), 400

    well.update(data)

    return jsonify(well), 200


@app.route("/api/wells/<int:well_id>", methods=["DELETE"])
def delete_well(well_id):

    well = next((w for w in wells if w["id"] == well_id), None)

    if well is None:
        return jsonify({"error": "Well not found"}), 404

    wells.remove(well)

    return jsonify({
        "message": "Well deleted successfully"
    }), 200


@app.route("/api/books/<string:isbn>", methods=["GET"])
def get_book(isbn):

    url = f"https://openlibrary.org/isbn/{isbn}.json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            return jsonify({"error": "Book not found"}), 404

        response.raise_for_status()

        return jsonify(response.json()), 200

    except requests.exceptions.Timeout:
        return jsonify({"error": "External API timed out"}), 504

    except requests.exceptions.RequestException:
        return jsonify({"error": "External API unavailable"}), 502

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "HTTP method not allowed"}), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500



if __name__ == "__main__":
    app.run(debug=True)
