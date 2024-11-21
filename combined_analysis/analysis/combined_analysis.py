import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load datasets
def load_datasets():
    print("Loading datasets...")
    garbage_data = pd.read_csv('/Users/kirangowda/Desktop/F21DL_coursework/garbage_classification/results/predictions.csv')
    climate_data = pd.read_csv('/Users/kirangowda/Desktop/F21DL_coursework/climate_analysis/results/preprocessed_climate_data.csv')
    pollution_data = pd.read_csv('/Users/kirangowda/Desktop/F21DL_coursework/pollution_analysis/results/preprocessed_pollution_data.csv')
# Debug prints to verify column names
    print("Columns in garbage_data:", garbage_data.columns)
    print("Columns in climate_data:", climate_data.columns)
    print("Columns in pollution_data:", pollution_data.columns)
    
    # Ensure the 'CountryName' column is consistent
    if 'CountryName' not in climate_data.columns and 'Country' in climate_data.columns:
        climate_data.rename(columns={'Country': 'CountryName'}, inplace=True)
    
    return garbage_data, climate_data, pollution_data

# Merge climate and pollution datasets
def merge_datasets(climate_data, pollution_data):
    merged_data = pd.merge(climate_data, pollution_data, on='CountryName', how='inner')
    return merged_data

# Analyze the merged climate and pollution data
def analyze_climate_pollution_data(merged_data):
    # Correlation matrix
    correlation_matrix = merged_data[['AverageTemperature', 'TotalWasteGenerated', 'OrganicWastePercent', 
                                      'GlassWastePercent', 'MetalWastePercent', 'PaperWastePercent', 
                                      'PlasticWastePercent']].corr()

    # Plot correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix of Climate and Pollution Data")
    plt.show()

# Analyze garbage data independently
def analyze_garbage_data(garbage_data):
    # Basic summary of garbage classification
    classification_counts = garbage_data['PredictedClass'].value_counts()
    print("Garbage Classification Counts:\n", classification_counts)
    
    # Plotting garbage classification distribution
    classification_counts.plot(kind='bar', color='skyblue')
    plt.xlabel("Garbage Type")
    plt.ylabel("Count")
    plt.title("Distribution of Garbage Types")
    plt.show()

# Main function
if __name__ == "__main__":
    garbage_data, climate_data, pollution_data = load_datasets()
    merged_data = merge_datasets(climate_data, pollution_data)
    
    # Save the merged data for reference
    merged_data.to_csv('/Users/kirangowda/Desktop/F21DL_coursework/combined_analysis/results/merged_climate_pollution_data.csv', index=False)
    print("Merged climate and pollution data saved as 'merged_climate_pollution_data.csv'")
    
    # Analyze the merged climate and pollution data
    analyze_climate_pollution_data(merged_data)
    
    # Analyze the garbage data independently
    analyze_garbage_data(garbage_data)