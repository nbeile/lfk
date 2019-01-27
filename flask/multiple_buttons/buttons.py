from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        button = request.form
        if "default" in button:
            return "default wurde gedrückt"
        if "primary" in button:
            return "primary wurde gedrückt"
        if "info" in button:
            return "info wurde gedrückt"
        if "warning" in button:
            return "warning wurde gedrückt"
        if "danger" in button:
            return "danger wurde gedrückt"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)