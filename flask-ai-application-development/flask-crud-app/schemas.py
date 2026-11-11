from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Well


class WellSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Well
        load_instance = True