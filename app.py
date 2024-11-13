from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.preprocessing import image
from utils.logger import log_classification
import tensorflow as tf
import numpy as np
import os

app = Flask(__name__)

model = tf.keras.models.load_model('garbage_classification_model.h5')

class_labels = ['battery', 'biological', 'brown-glass', 'cardboard', 'clothes', 'green-glass', 
                'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass']

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def classify_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)
    return class_labels[predicted_class[0]]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        try:
            file_path = os.path.join('static', file.filename)
            file.save(file_path)
            
            predicted_class = classify_image(file_path)
            log_classification(predicted_class)  # Log the classification result
            
            return render_template('result.html', filename=file.filename, label=predicted_class)
        except Exception as e:
            return f"Error processing image: {str(e)}"
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
