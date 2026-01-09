from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None

    if request.method == 'POST':
        file = request.files['image']
        angle = int(request.form['angle'])

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Open and rotate image
            img = Image.open(filepath)
            rotated = img.rotate(angle, expand=True)

            rotated_path = os.path.join(app.config['UPLOAD_FOLDER'], f"rotated_{file.filename}")
            rotated.save(rotated_path)

            image_url = rotated_path

    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
