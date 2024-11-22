import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_image_data_generator():
    """
    Creates an instance of ImageDataGenerator with predefined augmentations.
    """
    return ImageDataGenerator(
        rescale=1.0 / 255,       
        rotation_range=20,       
        width_shift_range=0.1,   
        height_shift_range=0.1,  
        shear_range=0.2,         
        zoom_range=0.2,          
        horizontal_flip=True,    
        fill_mode="nearest"      
    )

def load_training_data(dataset_dir, target_size=(128, 128), batch_size=32):
    """
    Loads and augments training data from the specified directory.
    
    Args:
        dataset_dir (str): Path to the dataset directory.
        target_size (tuple): Target size for resizing images.
        batch_size (int): Batch size for data generator.
    
    Returns:
        DirectoryIterator: The augmented training data.
    """
    datagen = create_image_data_generator()
    return datagen.flow_from_directory(
        dataset_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode="categorical",
        shuffle=True
    )

def save_class_labels(class_indices, labels_path):
    """
    Saves the class labels to a CSV file.

    Args:
        class_indices (dict): Dictionary mapping class labels to indices.
        labels_path (str): Path to save the labels CSV file.
    """
    os.makedirs(os.path.dirname(labels_path), exist_ok=True)
    with open(labels_path, "w") as f:
        f.writelines(f"{label},{index}\n" for label, index in class_indices.items())
    print(f"Labels saved to {labels_path}")

def preprocess_garbage_data():
    """
    Preprocess the garbage dataset, augment images, and save class labels.

    Returns:
        DirectoryIterator: The augmented training data.
    """
    dataset_dir = os.path.abspath("garbage_classification/dataset")
    labels_path = os.path.abspath("garbage_classification/results/classification_labels.csv")

    train_data = load_training_data(dataset_dir)
    save_class_labels(train_data.class_indices, labels_path)

    return train_data

if __name__ == "__main__":
    preprocess_garbage_data()
