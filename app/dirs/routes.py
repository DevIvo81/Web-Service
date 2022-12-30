from flask import Blueprint, render_template, request

dirs = Blueprint('dirs', __name__)

@dirs.route('/upload')
def upload():
    return render_template("upload.html")


@dirs.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)