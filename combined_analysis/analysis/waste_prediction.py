import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

def load_data(filepath):
    """ Load the merged data from a CSV file """
    return pd.read_csv(filepath)

def preprocess_data(data, features, target):
    """ Preprocess data by selecting features and the target, and handle missing values """
    data = data[features + [target]].dropna()
    X = data[features]
    y = data[target]
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """ Split data into training and testing sets """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X_train, y_train):
    """ Train a linear regression model """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """ Evaluate model performance and print errors """
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")
    return y_pred

def plot_results(y_test, y_pred):
    """ Plot actual vs predicted values """
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.6)
    plt.xlabel("Actual Organic Waste Percent")
    plt.ylabel("Predicted Organic Waste Percent")
    plt.title("Actual vs Predicted Organic Waste Percent")
    plt.show()

def main():
    print("Loading and preprocessing data...")
    data = load_data('combined_analysis/results/merged_climate_pollution_data.csv')
    features = ['AverageTemperature', 'PlasticWastePercent', 'GlassWastePercent']
    target = 'OrganicWastePercent'
    X, y = preprocess_data(data, features, target)
    
    print("Splitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    print("Training the model...")
    model = train_model(X_train, y_train)
    
    print("Evaluating the model...")
    y_pred = evaluate_model(model, X_test, y_test)
    
    print("Plotting the results...")
    plot_results(y_test, y_pred)

if __name__ == "__main__":
    main()
