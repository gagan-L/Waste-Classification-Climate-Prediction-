import pandas as pd
import os

def preprocess_pollution_data():
    # Load pollution data
    print("Loading pollution data...")
    df = pd.read_csv('../dataset/pollution_data.csv')
    print("Data loaded successfully.")
    
    # Verify columns
    print("Initial columns in the dataset:", df.columns)
    
    # Filter relevant columns
    df_filtered = df[['country_name', 
                      'total_msw_total_msw_generated_tons_year', 
                      'composition_food_organic_waste_percent', 
                      'composition_glass_percent', 
                      'composition_metal_percent', 
                      'composition_paper_cardboard_percent', 
                      'composition_plastic_percent']]
    
    df_filtered.columns = [
        'CountryName', 
        'TotalWasteGenerated', 
        'OrganicWastePercent', 
        'GlassWastePercent', 
        'MetalWastePercent', 
        'PaperWastePercent', 
        'PlasticWastePercent'
    ]
    
    df_filtered.dropna(inplace=True)
    
    df_filtered['TotalWasteGenerated'] = df_filtered['TotalWasteGenerated'] / df_filtered['TotalWasteGenerated'].max()

    df_filtered['OrganicWastePercent'] = df_filtered['OrganicWastePercent'] / 100.0
    df_filtered['GlassWastePercent'] = df_filtered['GlassWastePercent'] / 100.0
    df_filtered['MetalWastePercent'] = df_filtered['MetalWastePercent'] / 100.0
    df_filtered['PaperWastePercent'] = df_filtered['PaperWastePercent'] / 100.0
    df_filtered['PlasticWastePercent'] = df_filtered['PlasticWastePercent'] / 100.0

    output_path = '../results/preprocessed_pollution_data.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_filtered.to_csv(output_path, index=False)
    print(f"Data preprocessed and saved to: {output_path}")
if __name__ == "__main__":
    preprocess_pollution_data()
