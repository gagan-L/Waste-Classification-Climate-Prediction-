import pandas as pd
import os

def load_pollution_data(file_path):
    """
    Loads pollution data from a CSV file.

    Args:
        file_path (str): Path to the pollution data CSV file.

    Returns:
        pd.DataFrame: Loaded pollution data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Loading pollution data...")
    return pd.read_csv(file_path)

def preprocess_pollution_data(df):
    """
    Preprocesses the pollution data by filtering, renaming, normalizing, and cleaning.

    Args:
        df (pd.DataFrame): Raw pollution data.

    Returns:
        pd.DataFrame: Preprocessed pollution data.
    """
    print("Initial columns in the dataset:", df.columns)
    
    df_filtered = df[[
        'country_name', 
        'total_msw_total_msw_generated_tons_year', 
        'composition_food_organic_waste_percent', 
        'composition_glass_percent', 
        'composition_metal_percent', 
        'composition_paper_cardboard_percent', 
        'composition_plastic_percent'
    ]]
    
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
    
    df_filtered['TotalWasteGenerated'] /= df_filtered['TotalWasteGenerated'].max()
    
    # Convert waste composition percentages to decimal format
    percent_columns = [
        'OrganicWastePercent', 'GlassWastePercent', 
        'MetalWastePercent', 'PaperWastePercent', 'PlasticWastePercent'
    ]
    df_filtered[percent_columns] = df_filtered[percent_columns] / 100.0

    return df_filtered

def save_preprocessed_data(df, output_path):
    """
    Saves the preprocessed pollution data to a CSV file.

    Args:
        df (pd.DataFrame): Preprocessed pollution data.
        output_path (str): Path to save the preprocessed data.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data preprocessed and saved to: {output_path}")

def main_preprocess():
    """
    Main function to preprocess pollution data.
    """
    file_path = os.path.abspath('pollution_analysis/dataset/pollution_data.csv')
    output_path = os.path.abspath('pollution_analysis/results/preprocessed_pollution_data.csv')
    
    df = load_pollution_data(file_path)
    preprocessed_data = preprocess_pollution_data(df)
    save_preprocessed_data(preprocessed_data, output_path)

if __name__ == "__main__":
    main_preprocess()
