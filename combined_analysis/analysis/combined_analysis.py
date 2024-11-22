import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load datasets
def load_datasets():
    print("Loading datasets...")
    paths = {
        'garbage': 'garbage_classification/results/predictions.csv',
        'climate': 'climate_analysis/results/preprocessed_climate_data.csv',
        'pollution': 'pollution_analysis/results/preprocessed_pollution_data.csv'
    }
    data = {name: pd.read_csv(path) for name, path in paths.items()}
    
    # Debug prints to verify column names
    for name, df in data.items():
        print(f"Columns in {name}_data:", df.columns)
    
    # Ensure the 'CountryName' column is consistent in climate data
    if 'CountryName' not in data['climate'].columns and 'Country' in data['climate'].columns:
        data['climate'].rename(columns={'Country': 'CountryName'}, inplace=True)
    
    return data['garbage'], data['climate'], data['pollution']

# Merge climate and pollution datasets
def merge_datasets(climate_data, pollution_data):
    return pd.merge(climate_data, pollution_data, on='CountryName', how='inner')

# Analyze the merged climate and pollution data
def analyze_climate_pollution_data(merged_data):
    # Correlation matrix
    correlation_matrix = merged_data[['AverageTemperature', 'TotalWasteGenerated', 'OrganicWastePercent', 
                                      'GlassWastePercent', 'MetalWastePercent', 'PaperWastePercent', 
                                      'PlasticWastePercent']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix of Climate and Pollution Data")
    plt.show()

# Analyze garbage data independently
def analyze_garbage_data(garbage_data):
    # Summary of garbage classification counts
    classification_counts = garbage_data['PredictedClass'].value_counts()
    print("Garbage Classification Counts:\n", classification_counts)
    
    # Bar plot for garbage classification distribution
    plt.figure(figsize=(8, 6))
    classification_counts.plot(kind='bar', color='skyblue')
    plt.xlabel("Garbage Type")
    plt.ylabel("Count")
    plt.title("Distribution of Garbage Types")
    plt.show()

# Main function
def main():
    garbage_data, climate_data, pollution_data = load_datasets()
    merged_data = merge_datasets(climate_data, pollution_data)
    
    # Save the merged data for reference
    os.makedirs('combined_analysis/results', exist_ok=True)
    merged_data.to_csv('combined_analysis/results/merged_climate_pollution_data.csv', index=False)
    print("Merged climate and pollution data saved as 'merged_climate_pollution_data.csv'")
    
    analyze_climate_pollution_data(merged_data)
    analyze_garbage_data(garbage_data)

if __name__ == "__main__":
    main()
