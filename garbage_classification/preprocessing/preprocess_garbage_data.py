import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def preprocess_garbage_data():
    # Directory where the images are stored
    dataset_dir = '../dataset'
    
    # Set up data generator for image augmentation
    datagen = ImageDataGenerator(
        rescale=1./255,        # Normalize pixel values to [0, 1]
        rotation_range=20,     # Randomly rotate images
        width_shift_range=0.1, # Randomly shift images horizontally
        height_shift_range=0.1, # Randomly shift images vertically
        shear_range=0.2,       # Shear transformation
        zoom_range=0.2,        # Random zoom
        horizontal_flip=True,  # Randomly flip images horizontally
        fill_mode='nearest'
    )
    
    # Prepare training data using flow_from_directory
    train_data = datagen.flow_from_directory(
        dataset_dir,
        target_size=(128, 128),  # Resize images to 128x128
        batch_size=32,
        class_mode='categorical',  # Multiclass classification
        shuffle=True
    )
    
    # Save class indices for reference
    os.makedirs('../results', exist_ok=True)
    labels_path = '../results/classification_labels.csv'
    with open(labels_path, 'w') as f:
        for label, index in train_data.class_indices.items():
            f.write(f"{label},{index}\n")
    print(f"Labels saved to {labels_path}")

    return train_data

if __name__ == "__main__":
    preprocess_garbage_data()
