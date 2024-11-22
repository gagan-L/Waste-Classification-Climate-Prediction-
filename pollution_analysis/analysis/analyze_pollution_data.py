import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_preprocessed_data(file_path):
    """
    Loads preprocessed pollution data from a CSV file.

    Args:
        file_path (str): Path to the preprocessed pollution data CSV file.

    Returns:
        pd.DataFrame: Loaded pollution data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Loading preprocessed pollution data...")
    return pd.read_csv(file_path)

def plot_total_waste_generated(df, top_n=10):
    """
    Plots the top N countries by total waste generated.

    Args:
        df (pd.DataFrame): Preprocessed pollution data.
        top_n (int): Number of top countries to display.
    """
    top_countries = df.nlargest(top_n, 'TotalWasteGenerated')
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_countries, x='CountryName', y='TotalWasteGenerated')
    plt.title("Top 10 Countries by Total Waste Generated")
    plt.xlabel("Country")
    plt.ylabel("Normalized Total Waste Generated")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_waste_composition(df, country_name):
    """
    Plots the waste composition for a specific country.

    Args:
        df (pd.DataFrame): Preprocessed pollution data.
        country_name (str): Name of the country to analyze.
    """
    country_data = df[df['CountryName'] == country_name]
    if not country_data.empty:
        waste_types = [
            'OrganicWastePercent', 'GlassWastePercent', 
            'MetalWastePercent', 'PaperWastePercent', 'PlasticWastePercent'
        ]
        plt.figure(figsize=(8, 6))
        country_data[waste_types].T.plot(kind='bar', stacked=True, legend=False)
        plt.title(f"Waste Composition in {country_name}")
        plt.ylabel("Percentage")
        plt.xlabel("Waste Type")
        plt.xticks(range(len(waste_types)), waste_types, rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(f"No data available for {country_name}.")

def main_analyze():
    """
    Main function to analyze pollution data and generate visualizations.
    """
    file_path = os.path.abspath('pollution_analysis/results/preprocessed_pollution_data.csv')
    df = load_preprocessed_data(file_path)
    
    # Plot total waste generated
    plot_total_waste_generated(df)

    # Plot waste composition for a specific country
    country_name = "United States"
    plot_waste_composition(df, country_name)

if __name__ == "__main__":
    main_analyze()
