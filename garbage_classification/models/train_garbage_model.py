import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(12, activation='softmax')  # 12 categories
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(train_data):
    model = build_model()
    model.summary()
    
    # Train the model
    model.fit(train_data, epochs=10, steps_per_epoch=train_data.samples // train_data.batch_size)
    
    # Save the model
    model.save('../results/garbage_classification_model.h5')
    print("Model saved to ../results/garbage_classification_model.h5")

if __name__ == "__main__":
    # Load the preprocessed data
    datagen = ImageDataGenerator(rescale=1./255)
    train_data = datagen.flow_from_directory(
        '../dataset',
        target_size=(128, 128),
        batch_size=32,
        class_mode='categorical',
        shuffle=True
    )
    
    # Train the model
    train_model(train_data)
