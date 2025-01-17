import json
import pandas as pd

# Function to read and parse JSON data from a file
def parse_aare_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Function to flatten the JSON data and create a DataFrame
def flatten_aare_data(data):
    aare_data = data['aare']
    coordinates = aare_data.pop('coordinates')
    temperature_scale = aare_data.pop('temperature_scale')
    
    # Flatten the main data
    flat_data = {**aare_data, **coordinates}
    
    # Create DataFrame for the main data
    df_main = pd.DataFrame([flat_data])
    
    # Create DataFrame for the temperature scale
    df_temp_scale = pd.DataFrame(temperature_scale)
    
    return df_main, df_temp_scale

# Example usage
file_path = 'd:/Github/playground_data_engineering/aare_data.json'
aare_data = parse_aare_data(file_path)
df_main, df_temp_scale = flatten_aare_data(aare_data)

# Print the DataFrames
print("Main DataFrame:")
print(df_main)
print("\nTemperature Scale DataFrame:")
print(df_temp_scale)