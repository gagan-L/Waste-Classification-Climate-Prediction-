import os
import tensorflow as tf
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_model(model_path):
    """
    Loads a pre-trained Keras model from the specified path.

    Args:
        model_path (str): Path to the model file.

    Returns:
        tf.keras.Model: Loaded Keras model.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return tf.keras.models.load_model(model_path)

def predict_classes(model, data_generator):
    """
    Predicts classes for the images in the data generator using the provided model.

    Args:
        model (tf.keras.Model): Trained Keras model.
        data_generator (DirectoryIterator): Data generator containing images.

    Returns:
        list: List of dictionaries containing image filenames and their predicted classes.
    """
    predictions = model.predict(data_generator, verbose=1)
    predicted_classes = predictions.argmax(axis=1)
    return [
        {"Image": filename, "PredictedClass": predicted_class}
        for filename, predicted_class in zip(data_generator.filenames, predicted_classes)
    ]

def save_predictions_to_csv(predictions, output_path):
    """
    Saves predictions to a CSV file.

    Args:
        predictions (list): List of dictionaries containing filenames and predicted classes.
        output_path (str): Path to save the predictions CSV file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_results = pd.DataFrame(predictions)
    df_results.to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")

def create_data_generator(data_dir, target_size=(128, 128), batch_size=32):
    """
    Creates a data generator for image preprocessing.

    Args:
        data_dir (str): Path to the dataset directory.
        target_size (tuple): Target size for resizing images.
        batch_size (int): Batch size for data generator.

    Returns:
        DirectoryIterator: Data generator for the images.
    """
    datagen = ImageDataGenerator(rescale=1.0 / 255)
    return datagen.flow_from_directory(
        data_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode="categorical",
        shuffle=False
    )

def main():
    """
    Main function to load the model, predict classes, and save predictions.
    """
    model_path = os.path.abspath("../results/garbage_classification_model.h5")
    data_dir = os.path.abspath("../dataset")
    output_csv_path = os.path.abspath("../results/predictions.csv")

    model = load_model(model_path)
    train_data = create_data_generator(data_dir)

    predictions = predict_classes(model, train_data)
    save_predictions_to_csv(predictions, output_csv_path)

if __name__ == "__main__":
    main()
