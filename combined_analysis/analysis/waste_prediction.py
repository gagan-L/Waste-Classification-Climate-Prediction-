# waste_prediction.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Load merged data
def load_data():
    # Load the merged data from CSV (ensure this file exists in the specified path)
    data = pd.read_csv('/Users/kirangowda/Desktop/F21DL_coursework/combined_analysis/results/merged_climate_pollution_data.csv')
    return data

# Preprocess data: select relevant features and target, handle missing values
def preprocess_data(data):
    # Selecting features based on the correlation analysis and domain knowledge
    features = ['AverageTemperature', 'PlasticWastePercent', 'GlassWastePercent']
    target = 'OrganicWastePercent'
    
    # Drop rows with missing values in the selected columns
    data = data[features + [target]].dropna()
    
    X = data[features]
    y = data[target]
    
    return X, y

# Split data into training and testing sets
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Train a linear regression model
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Evaluate model performance
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")
    
    return y_pred

# Plot actual vs predicted values
def plot_results(y_test, y_pred):
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.6)
    plt.xlabel("Actual OrganicWastePercent")
    plt.ylabel("Predicted OrganicWastePercent")
    plt.title("Actual vs Predicted OrganicWastePercent")
    plt.show()

# Main pipeline execution
if __name__ == "__main__":
    # Load and preprocess data
    print("Loading and preprocessing data...")
    data = load_data()
    X, y = preprocess_data(data)
    
    # Split data
    print("Splitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Train the model
    print("Training the model...")
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    print("Evaluating the model...")
    y_pred = evaluate_model(model, X_test, y_test)
    
    # Plot results
    print("Plotting the results...")
    plot_results(y_test, y_pred)
