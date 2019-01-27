from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

# Pfad dieses Python-Programms
path_this_file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
path_this_file = os.path.join(path_this_file, "upload", "uploads")

print(path_this_file)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = path_this_file

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)