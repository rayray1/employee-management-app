# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Department, Role


# admin form-edit/add a department
class DepartmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


# admin form-add/edit a role
class RoleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


# admin form-assign roles n departments
class EmployeeAssignForm(FlaskForm):
    department = QuerySelectField(query_factory=lambda: Department.query.all(), get_label='name')
    role = QuerySelectField(query_factory=lambda: Role.query.all(), get_label='name')
    submit = SubmitField('Submit')
