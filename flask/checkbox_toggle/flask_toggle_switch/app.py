from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import BooleanField

app = Flask(__name__)
app.config["SECRET_KEY"] = "g7QZmwiNTnxF9OCg"

class TestForm(FlaskForm):
    someSwitchOption001 = BooleanField(default=False) # default = True fuer gesetzten switch

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        try:
            check_value = request.form['someSwitchOption001']
        except:
            check_value = "n"
        return "{}".format(check_value)

    form = TestForm()
    return render_template('hello.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)