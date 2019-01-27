from flask import Flask, render_template, request

app = Flask(__name__)

inhalt = '''<option data-subtext="Frankfurter Börse">Deutsche Post AG</option><option data-subtext="Frankfurter Börse">Allianz SE</option><option data-subtext="Frankfurter Börse">Bayerische Motoren Werke Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">Deutsche Telekom AG</option><option data-subtext="Frankfurter Börse">Fresenius Medical Care AG & Co. KGaA</option><option data-subtext="Frankfurter Börse">BASF SE</option><option data-subtext="Frankfurter Börse">Henkel AG & Co. KGaA</option><option data-subtext="Frankfurter Börse">Linde Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">SAP SE</option><option data-subtext="Frankfurter Börse">Deutsche Bank Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">Bayer Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">Volkswagen AG</option><option data-subtext="Frankfurter Börse">HeidelbergCement AG</option><option data-subtext="Frankfurter Börse">Fresenius SE & Co. KGaA</option><option data-subtext="Frankfurter Börse">MERCK Kommanditgesellschaft auf Aktien</option><option data-subtext="Frankfurter Börse">Beiersdorf Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">Siemens Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">Münchener Rückversicherungs-Gesellschaft Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">Deutsche Börse Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">Vonovia SE</option><option data-subtext="Frankfurter Börse">E.ON SE</option><option data-subtext="Frankfurter Börse">Daimler AG</option><option data-subtext="Frankfurter Börse">adidas AG</option><option data-subtext="Frankfurter Börse">Wirecard AG</option><option data-subtext="Frankfurter Börse">RWE Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">Infineon Technologies AG</option><option data-subtext="Frankfurter Börse">Covestro AG</option><option data-subtext="Frankfurter Börse">thyssenkrupp AG</option><option data-subtext="Frankfurter Börse">Continental Aktiengesellschaft</option><option data-subtext="Frankfurter Börse">Deutsche Lufthansa AG</option>'''


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        auswahl = request.form['selectpicker']
        print(auswahl)
    return render_template('index.html', inhalt=inhalt)


if __name__ == '__main__':
    app.run(debug=True)
