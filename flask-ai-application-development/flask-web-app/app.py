
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

if not app.secret_key:
    raise RuntimeError("SECRET_KEY environment variable is not configured")



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
    search = request.args.get("search", "").strip().lower()

    filtered_wells = [
        well for well in wells
        if search in well["name"].lower()
        or search in well["field"].lower()
    ]

    return render_template(
        "dashboard.html",
        wells=filtered_wells,
        all_wells=wells,
        search=search
    )



@app.route("/well/<int:well_id>")
def well_details(well_id):
    well = next(
        (well for well in wells if well["id"] == well_id),
        None
    )

    if well is None:
        return "Well not found", 404

    return render_template("well_details.html", well=well)



@app.route("/add-well", methods=["GET", "POST"])
def add_well():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        field = request.form.get("field", "").strip()
        depth = request.form.get("depth_m", "").strip()
        production = request.form.get("production_bopd", "").strip()

        if not name or not field or not depth or not production:
            flash("All fields are required.", "error")
            return redirect(url_for("add_well"))

        try:
            depth = float(depth)
            production = float(production)

            if depth <= 0 or production < 0:
                raise ValueError

        except ValueError:
            flash("Enter valid positive depth and non-negative production values.", "error")
            return redirect(url_for("add_well"))

        new_well = {
            "id": max(w["id"] for w in wells) + 1,
            "name": name,
            "field": field,
            "depth_m": depth,
            "production_bopd": production
        }

        wells.append(new_well)

        return redirect(url_for("dashboard"))

    return render_template("add_well.html")


if __name__ == "__main__":
    app.run(debug=True)
