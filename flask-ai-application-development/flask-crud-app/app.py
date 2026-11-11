
from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate
from models import db, Well
from forms import WellForm
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)

migrate = Migrate(app, db)

class PetroWellAdminIndex(AdminIndexView):

    @expose("/")
    def index(self):
        total_wells = Well.query.count()

        total_production = db.session.query(
            db.func.sum(Well.production_bopd)
        ).scalar() or 0

        return self.render(
            "admin/index.html",
            total_wells=total_wells,
            total_production=total_production
        )


admin = Admin(
    app,
    name="PetroWell Admin",
    index_view=PetroWellAdminIndex()
)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///petro_wells.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "development-secret-key"

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("index.html")


# READ: Display all wells
@app.route("/wells")
def wells():
    all_wells = Well.query.order_by(Well.id.desc()).all()
    return render_template("wells.html", wells=all_wells)


# CREATE: Add a new well
@app.route("/wells/add", methods=["GET", "POST"])
def add_well():
    form = WellForm()

    if form.validate_on_submit():
        well = Well(
            name=form.name.data,
            field=form.field.data,
            depth_m=form.depth_m.data,
            production_bopd=form.production_bopd.data,
            status=form.status.data
        )

        db.session.add(well)
        db.session.commit()

        flash("Well added successfully!", "success")
        return redirect(url_for("wells"))

    return render_template("add_well.html", form=form)


# UPDATE: Edit an existing well
@app.route("/wells/edit/<int:well_id>", methods=["GET", "POST"])
def edit_well(well_id):
    well = db.get_or_404(Well, well_id)
    form = WellForm(obj=well)

    if form.validate_on_submit():
        form.populate_obj(well)
        db.session.commit()

        flash("Well updated successfully!", "success")
        return redirect(url_for("wells"))

    return render_template("edit_well.html", form=form, well=well)


# DELETE: Remove an existing well
@app.route("/wells/delete/<int:well_id>", methods=["POST"])
def delete_well(well_id):
    well = db.get_or_404(Well, well_id)

    db.session.delete(well)
    db.session.commit()

    flash("Well deleted successfully!", "success")
    return redirect(url_for("wells"))


if __name__ == "__main__":
    app.run(debug=True)
