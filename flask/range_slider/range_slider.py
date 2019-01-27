from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import NumberRange

app = Flask(__name__)
app.config["SECRET_KEY"] = "g7QZmwiNTnxF9OCg"

class TestForm(FlaskForm):
    days = IntegerRangeField('Tage', default=30)#, validators=[NumberRange(min=0, max=365)]

@app.route("/")
def home():
    form = TestForm(csrf_enabled=False)
    return render_template('hello.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)