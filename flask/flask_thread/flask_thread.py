from flask import Flask, render_template, request
import time
import threading


app = Flask(__name__)
app.config["SCHEDULER_API_ENABLED"] = True

# Event erstellen, das den Thread stoppen kann.
run_event = threading.Event()
# Eventflagge auf True setzen
run_event.set()

i = 0


def test_job(arg, run_event):
    global i
    i = i + 1

    print("Saying hello {0} for the {1}. time".format(arg, i))
    time.sleep(2)


def while_job(i_max, run_event):
    global i
    while True:

        # Funktion abbrechen, wenn [Strg] + [C] gedrueckt wurde
        if run_event.is_set():
            pass
        else:
            break

        print("i_max von {0} noch nicht erreicht. Schritt {1}".format(i_max, i))
        i = i + 1
        time.sleep(2)


@app.route("/", methods=["GET", "POST"])
def home():
    global run_event

    if request.method == "POST":
        button = request.form

        if "on" in button:
            print("Adding job")
            t_test_job = threading.Thread(target=test_job, args=("World", run_event))
            t_while_job = threading.Thread(target=while_job, args=(5, run_event))
            # t_test_job.start()
            t_while_job = threading.Thread(target=while_job, args=(5, run_event))
            t_while_job.start()
            return render_template('index.html')

        if "off" in button:
            print("Removing job")
            # Eventflagge auf False setzen
            run_event.clear()
            # Event erstellen, das den Thread stoppen kann.
            run_event = threading.Event()
            # Eventflagge auf True setzen
            run_event.set()
            return render_template('index.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
