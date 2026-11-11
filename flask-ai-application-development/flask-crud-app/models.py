
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Well(db.Model):
    __tablename__ = "wells"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    field = db.Column(db.String(100), nullable=False)
    depth_m = db.Column(db.Float, nullable=False)
    production_bopd = db.Column(db.Float, nullable=False, default=0)
    status = db.Column(db.String(30), nullable=False, default="Active")

    def __repr__(self):
        return f"<Well {self.name}>"
