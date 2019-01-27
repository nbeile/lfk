from flask import Flask, render_template, request, flash, redirect
from werkzeug import secure_filename
import os

# Pfad dieses Python-Programms
path_this_file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
path_this_file = os.path.join(path_this_file, "upload_flash", "uploads")

print(path_this_file)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = path_this_file
ALLOWED_EXTENSIONS = set(['txt'])
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'test' not in request.files:
            flash('Es wurde keine Datei übermittelt. Stellen Sie sicher, dass eine Datei ausgewählt wurde.', "danger") #2. Parameter "Category": success (gruen), info (blau), warning (gelb), danger (rot)
            return redirect(request.url)
        f = request.files['test']
        # if user does not select file, browser also
        # submit an empty part without filename
        if f.filename == '':
            flash('Keine Datei ausgewählt', "danger") #2. Parameter "Category": success (gruen), info (blau), warning (gelb), danger (rot)
            return redirect(request.url)
        if allowed_file(f.filename) == False:
            flash("Falsche Datei - muss mit '.txt' enden", "danger") #2. Parameter "Category": success (gruen), info (blau), warning (gelb), danger (rot)
            return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return 'file uploaded successfully'
            flash("Datei {0} erfolgreich importiert".format(f.filename), "success") #2. Parameter "Category": success (gruen), info (blau), warning (gelb), danger (rot)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)