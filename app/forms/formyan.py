from wtforms import Form,StringField,IntegerField,validators
from wtforms.validators import required

class SearchForm(Form):
    q=StringField(validators=[required])
    page=IntegerField(validators=[required])