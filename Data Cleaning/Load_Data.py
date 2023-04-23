import os
import pandas as pd

def import_weather_data(path_weather, path_dir):
    path_weather = os.path.join(path_dir, path_weather)
    csv_files_weather = [file for file in os.listdir(path_weather) if file.endswith('.csv')]
    data_weather = {}
    i = 1
    for file in csv_files_weather:
        filepath = os.path.join(path_weather, file)
        df = pd.read_csv(filepath)
        key_name = "Q" + str(i)
        i = i + 1
        data_weather[key_name] = df
    return data_weather

def import_noise_data(path_noise, path_dir):
    path_noise = os.path.join(path_dir, path_noise)
    csv_files_noise = [file for file in os.listdir(path_noise) if file.endswith('.csv')]
    data_noise = {}
    for file in csv_files_noise:
        filepath = os.path.join(path_noise, file)
        df = pd.read_csv(filepath, delimiter = ";")
        data_noise[file] = df
    return data_noise

def load_data(  path_weather = "Raw Data\Weather Data",
                path_noise = "Raw Data\\Noise Data",
                load_weather = True,
                load_noise = True):
    output = {}
    #Rooth path of the file
    path_dir = os.path.dirname(__file__)   

    # Loading in the weather data
    if load_weather:
        output["weather"] = import_weather_data(path_weather, path_dir)

    # Loading in the noise data
    if load_noise:
        output["noise"] = import_noise_data(path_noise, path_dir)
        
    return output

data = load_data()
