print("gestartet")

# notwendige Bibliothek (pandas_datareader) importieren
import pandas_datareader.data as web
from flask import Flask, render_template
from bokeh.plotting import figure, show
from bokeh.embed import components
print("Bibliotheken importiert")


app = Flask(__name__)

# figure erstellen
def make_figure():
    # Chart als Dataframe df erzeugen
    symbol = 'VOW.DE' # Volkswagen Aktie
    endpoint = 'quandl'
    start = '2018-11-05'
    end = '2018-12-02'
    # Dataframe df erstellen
    df = web.DataReader(symbol, endpoint, start, end)
    # Reihenfolge umkehren
    df1 = df.iloc[::-1]
    # Neuen Index erstellen
    df2 = df1.reset_index()
    # Bokeh-Figure erstellen
    plot = figure(width=750, height=450, title='Hallo Welt',
                  x_axis_label='date')
    # Bokeh-Plot erstellen
    plot.line(df2["Date"], df2["Last"])
    return plot

@app.route('/')
def greet():
    script, div = components(make_figure())

    return render_template('index.html', script=script, div=div)


if __name__ == '__main__':
    app.run(debug=True)