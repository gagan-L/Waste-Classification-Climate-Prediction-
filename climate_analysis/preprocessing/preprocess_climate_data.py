import pandas as pd
import os

def load_climate_data(file_path):
    """
    Loads climate data from a CSV file.

    Args:
        file_path (str): Path to the climate data CSV file.

    Returns:
        pd.DataFrame: Loaded climate data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Loading climate data...")
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    Preprocesses the climate data by extracting the year and normalizing temperatures.

    Args:
        df (pd.DataFrame): Climate data.

    Returns:
        pd.DataFrame: Preprocessed climate data grouped by country and year.
    """
    # Extract year from date and drop rows with invalid dates
    df['Year'] = pd.to_datetime(df['dt'], errors='coerce').dt.year
    df = df.dropna(subset=['Year'])

    # Group by country and year, and calculate mean temperature
    df_yearly = df.groupby(['Country', 'Year'])['AverageTemperature'].mean().reset_index()

    # Normalize the average temperature
    temp_min = df_yearly['AverageTemperature'].min()
    temp_max = df_yearly['AverageTemperature'].max()
    df_yearly['NormalizedTemperature'] = (df_yearly['AverageTemperature'] - temp_min) / (temp_max - temp_min)
    
    return df_yearly

def save_preprocessed_data(df, output_path):
    """
    Saves the preprocessed climate data to a CSV file.

    Args:
        df (pd.DataFrame): Preprocessed climate data.
        output_path (str): Path to save the preprocessed data.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

def preprocess_climate_data():
    """
    Main function to preprocess climate data.
    """
    file_path = os.path.abspath('climate_analysis/dataset/climate_data.csv')
    output_path = os.path.abspath('climate_analysis/results/preprocessed_climate_data.csv')

    # Load, preprocess, and save climate data
    climate_data = load_climate_data(file_path)
    preprocessed_data = preprocess_data(climate_data)
    save_preprocessed_data(preprocessed_data, output_path)

if __name__ == "__main__":
    preprocess_climate_data()
