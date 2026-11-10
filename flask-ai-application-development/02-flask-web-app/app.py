
from flask import Flask, render_template

app = Flask(__name__)

wells = [
    {
        "id": 1,
        "name": "Well A",
        "field": "Escravos",
        "depth_m": 2500,
        "production_bopd": 1800
    },
    {
        "id": 2,
        "name": "Well B",
        "field": "Ughelli",
        "depth_m": 3200,
        "production_bopd": 2400
    },
    {
        "id": 3,
        "name": "Well C",
        "field": "Forcados",
        "depth_m": 2800,
        "production_bopd": 2100
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", wells=wells)


@app.route("/well/<int:well_id>")
def well_details(well_id):
    well = next(
        (well for well in wells if well["id"] == well_id),
        None
    )

    if well is None:
        return "Well not found", 404

    return render_template("well_details.html", well=well)


if __name__ == "__main__":
    app.run(debug=True)
