from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    flash("flash test!!!!", "info") #2. Parameter "Category": success (gruen), info (blau), warning (gelb), danger (rot)
    return render_template("index.html")

if __name__=="__main__":
	app.run(debug=True)