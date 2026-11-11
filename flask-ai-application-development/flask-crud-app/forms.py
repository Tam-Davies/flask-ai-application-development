
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length


class WellForm(FlaskForm):
    name = StringField(
        "Well Name",
        validators=[DataRequired(), Length(max=100)]
    )

    field = StringField(
        "Field",
        validators=[DataRequired(), Length(max=100)]
    )

    depth_m = FloatField(
        "Depth (m)",
        validators=[DataRequired(), NumberRange(min=0.01)]
    )

    production_bopd = FloatField(
        "Production (BOPD)",
        validators=[DataRequired(), NumberRange(min=0)]
    )

    status = SelectField(
        "Status",
        choices=[
            ("Active", "Active"),
            ("Shut-in", "Shut-in"),
            ("Abandoned", "Abandoned")
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField("Save Well")
