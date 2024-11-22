import tensorflow as tf
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def save_predictions(train_data):
    model = tf.keras.models.load_model('garbage_classification/results/garbage_classification_model.h5')
    predictions = model.predict(train_data)
    predicted_classes = predictions.argmax(axis=1)
    
    results = []
    for i, (filename, prediction) in enumerate(zip(train_data.filenames, predicted_classes)):
        results.append({'Image': filename, 'PredictedClass': prediction})
    
    df_results = pd.DataFrame(results)
    df_results.to_csv('garbage_classification/results/predictions.csv', index=False)
    print("Predictions saved to garbage_classification/results/predictions.csv")

if __name__ == "__main__":
    datagen = ImageDataGenerator(rescale=1./255)
    train_data = datagen.flow_from_directory(
        'garbage_classification/dataset',
        target_size=(128, 128),
        batch_size=32,
        class_mode='categorical',
        shuffle=False
    )
    
    save_predictions(train_data)
