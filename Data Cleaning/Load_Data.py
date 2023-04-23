import os
import pandas as pd


def load_data(path_weather = "", path_noise = "", path_dir = os.path.dirname(__file__)):

    return(path_dir)
    # csv_files_weather = [file for file in os.listdir(path_weather) if file.endswith('.csv')]
    # data_weather = {}
    # i = 1
    # for file in csv_files_weather:
    #     filepath = os.path.join(path_weather, file)
    #     df = pd.read_csv(filepath)
    #     key_name = "Q" + str(i)
    #     i = i + 1
    #     data_weather[key_name] = df

    # csv_files_noise = [file for file in os.listdir(path_noise) if file.endswith('.csv')]
    # data_noise = {}
    # for file in csv_files_noise:
    #     filepath = os.path.join(path_noise, file)
    #     df = pd.read_csv(filepath, delimiter = ";")
    #     data_noise[file] = df
    
    # return data_weather, data_noise

print(load_data())