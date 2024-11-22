import pandas as pd
import matplotlib.pyplot as plt 

def combined_analysis():
    garbage_df = pd.read_csv('garbage_classification/results/classification_labels.csv')
    climate_df = pd.read_csv('climate_analysis/results/preprocessed_climate_data.csv')
    pollution_df = pd.read_csv('pollution_analysis/results/preprocessed_pollution_data.csv')

   # Merge climate and pollution data on country names
    merged_df = pollution_df.merge(climate_df, left_on="country_name", right_on="Country", how="inner")
    
    # Analyze Correlation between Temperature and Waste Generation
    print("Correlation between Temperature and Total Waste Generated:")
    correlation = merged_df['AverageTemperature'].corr(merged_df['TotalWasteGenerated'])
    print(f"Correlation: {correlation}")
    
    # Plot Temperature vs. Waste Generation
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_df['AverageTemperature'], merged_df['TotalWasteGenerated'], alpha=0.5)
    plt.xlabel("Average Temperature")
    plt.ylabel("Total Waste Generated (normalized)")
    plt.title("Average Temperature vs. Total Waste Generation by Country")
    plt.show()
    
    # Visualize Waste Composition for a Specific Country (e.g., Argentina)
    sample_country = merged_df[merged_df['country_name'] == 'Argentina']  # Replace with the country of your choice
    waste_types = ['OrganicWastePercent', 'GlassWastePercent', 'MetalWastePercent', 
                   'PaperWastePercent', 'PlasticWastePercent']
    
    sample_country[waste_types].plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title("Waste Composition in Argentina")
    plt.xlabel("Data Points")
    plt.ylabel("Percentage")
    plt.legend(title="Waste Type")
    plt.show()

# Run the combined analysis
if __name__ == "__main__":
    combined_analysis()
