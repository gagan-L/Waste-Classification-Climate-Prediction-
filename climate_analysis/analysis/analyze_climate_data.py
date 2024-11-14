import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_climate_data():
    # Load preprocessed data
    file_path = '../results/preprocessed_climate_data.csv'
    df = pd.read_csv(file_path)
    print("Data loaded successfully for analysis.")

    # Plot temperature trends for a few sample countries
    countries = ['India', 'United States', 'China', 'Brazil', 'Germany']
    plt.figure(figsize=(12))
    for country in countries:
        country_data = df[df['Country'] == country]
        sns.lineplot(data=country_data, x='Year', y='NormalizedTemperature', label=country)

    plt.title("Normalized Average Temperature Trends Over Time")
    plt.xlabel("Year")
    plt.ylabel("Normalized Temperature")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    analyze_climate_data()
