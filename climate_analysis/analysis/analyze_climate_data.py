import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_preprocessed_data(file_path):
    """
    Loads preprocessed climate data from the specified file path.

    Args:
        file_path (str): Path to the preprocessed climate data file.

    Returns:
        pd.DataFrame: Loaded climate data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Data loaded successfully for analysis.")
    return pd.read_csv(file_path)

def plot_temperature_trends(df, countries, output_path=None):
    """
    Plots normalized average temperature trends over time for selected countries.

    Args:
        df (pd.DataFrame): Preprocessed climate data.
        countries (list): List of countries to plot.
        output_path (str, optional): Path to save the plot. Defaults to None.
    """
    plt.figure(figsize=(12, 6))
    for country in countries:
        country_data = df[df['Country'] == country]
        sns.lineplot(data=country_data, x='Year', y='NormalizedTemperature', label=country)
    
    plt.title("Normalized Average Temperature Trends Over Time")
    plt.xlabel("Year")
    plt.ylabel("Normalized Temperature")
    plt.legend()
    
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path)
        print(f"Plot saved to {output_path}")
    else:
        plt.show()

def analyze_climate_data():
    """
    Main function to analyze climate data and plot temperature trends.
    """
    file_path = os.path.abspath("climate_analysis/results/preprocessed_climate_data.csv")
    output_path = os.path.abspath("climate_analysis/results/temperature_trends.png")
    
    # Load data
    climate_data = load_preprocessed_data(file_path)
    
    # Countries to analyze
    countries = ['India', 'United States', 'China', 'Brazil', 'Germany']
    
    # Plot trends
    plot_temperature_trends(climate_data, countries, output_path=output_path)

if __name__ == "__main__":
    analyze_climate_data()
