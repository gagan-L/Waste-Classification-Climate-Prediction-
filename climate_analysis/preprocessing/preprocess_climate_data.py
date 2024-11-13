import pandas as pd
import os

def preprocess_climate_data():
    print("Loading climate data...")
    file_path = '../dataset/climate_data.csv'
    df = pd.read_csv(file_path)

    df['Year'] = pd.to_datetime(df['dt'], errors='coerce').dt.year
    df = df.dropna(subset=['Year'])

    df_yearly = df.groupby(['Country', 'Year'])['AverageTemperature'].mean().reset_index()
    
    df_yearly['NormalizedTemperature'] = (df_yearly['AverageTemperature'] - df_yearly['AverageTemperature'].min()) / \
                                          (df_yearly['AverageTemperature'].max() - df_yearly['AverageTemperature'].min())


if __name__ == "__main__":
    preprocess_climate_data()
