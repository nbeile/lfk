from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms.fields.html5 import DecimalRangeField

app = Flask(__name__)
# app.config["SECRET_KEY"] = "g7QZmwiNTnxF9OCg"

'''
class TestForm(FlaskForm):
    age = DecimalRangeField('Age', default=0)
'''

@app.route("/")
def home():
    # form = TestForm(csrf_enabled=False)
    # return render_template('hello.html', form=form)
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug = True)