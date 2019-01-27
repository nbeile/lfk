from flask import Flask, render_template, request
import json
import os


app = Flask(__name__)

# Lise, das uebertragen wird:
uebertragen = ["Null", "Eins", "Zwei", "Drei", "Vier", "Fünf", "Sechs"]

uebertragen = [
    {"0": "Null"},
    {"2": "Eins"},
    {"2": "Zwei"},
    {"3": "Drei"},
    {"4": "Vier"},
    {"5": "Fünf"},
    {"6": "Sechs"}
]


@app.route('/')
def index():
    with open(os.path.join("einstellungen", "voreinstellungen.txt")) as json_file:
        voreinstellungen_data = json.load(json_file)
    ordem = str(voreinstellungen_data["order"])

    print(ordem)

    return render_template('index2.html', ordem=ordem, uebertragen=uebertragen)


@app.route('/post', methods=['GET', 'POST'])
def post():
    json_input = request.json
    print(json_input)
    x = json_input.replace('item[]=', ',')
    y = x.replace('&,', '')
    final = y.replace(',', '')
    final_dict = {}
    final_dict["order"] = final

    with open(os.path.join("einstellungen", "voreinstellungen.txt"), 'w') as outfile:
        json.dump(final_dict, outfile)

    return str('')


if __name__ == '__main__':
    app.run(debug=True)
