import os
import pandas as pd

def import_weather_data(weather_path, dir_path):
    weather_path = os.path.join(dir_path, weather_path)
    csv_files_weather = [file for file in os.listdir(weather_path) if file.endswith('.csv')]
    data_weather = {}
    i = 1
    for file in csv_files_weather:
        filepath = os.path.join(weather_path, file)
        df = pd.read_csv(filepath)
        key_name = "Q" + str(i)
        i = i + 1
        data_weather[key_name] = df
    return data_weather

def import_noise_data(noise_path, dir_path, month = "April"):
    noise_path = os.path.join(dir_path, noise_path)
    #The files are in multiple maps seperated by month.    
    noise_data = {}

    filepath_month = os.path.join(noise_path, month)
    csv_files_weather = [file for file in os.listdir(filepath_month) if file.endswith('.csv')]

    for file in csv_files_weather:
        filepath = os.path.join(filepath_month, file)
        df = pd.read_csv(filepath, delimiter = ";")
        noise_data[file] = df
        print( f"Loaded file {file} from month {month}")
    return noise_data

def import_data(    weather_path = "Raw Data\Weather Data"  ,
                    noise_path = "Raw Data\\Noise Data"     ,
                    noise_month = "April"                   ,
                    load_weather = True                     ,
                    load_noise = True                       ,):
    
    output = {}
    #Rooth path of the file
    dir_path = os.path.dirname(__file__)   

    # Loading in the weather data
    if load_weather:
        output["weather"] = import_weather_data(weather_path, dir_path)

    # Loading in the noise data
    if load_noise:
        output["noise"] = import_noise_data(noise_path, dir_path, noise_month)
        
    return output

data = import_noise_data("Raw Data\\Noise Data", os.path.dirname(__file__))
