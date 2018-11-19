import sklearn
import csv
from os import listdir
import numpy as np
from geopy.geocoders import Nominatim
import plotly
plotly.tools.set_credentials_file(username='haoran88', api_key='Dvsr2pAhI49jMnWPa6Vo')
import pandas as pd
from os import listdir
from src.data import EDA
import csv
from time import time
import os

def Each_data(Main_Data_Path, data_file_name):
    tmp_dataframe_list = []
    tmp_csv_list = []

    for j in data_file_name:
        Each_file = Main_Data_Path + j

        with open(Each_file) as file:
            tmp_dataframe_list.append((str(j), pd.read_csv(file)))
            tmp_csv_list.append((str(j), csv.reader(file)))
    Data_frame = dict(tmp_dataframe_list)
    Data_csv = dict(tmp_csv_list)

    return Data_frame,Data_csv

def Load_Single(tNum, type_file):

    timesName = '-' + str(tNum) + '_'
    fileName = '../Data/raw/Engagement of Cyber Serurity/dataset201819/cyber-security' + timesName + type_file + '.csv'
    singlefile = pd.read_csv(fileName)

    return singlefile


def Data_Type(data_file_name):
    num_times = 1
    times_list = []
    times_count = []
    tmp_data = []
    length_each = []
    nameCount = []
    just_count = 0

    for i in range(len(data_file_name) + 1):

        if i >= len(data_file_name):
            times_list.append(tmp_data)
            nameCount.append('Term_' + str(num_times))
        else:
            if int(data_file_name[i][15]) != num_times:
                length_each.append(i - just_count)
                nameCount.append('Term_' + str(num_times))
                num_times += 1
                times_list.append(tmp_data)
                tmp_data = []
                just_count = i
            # print(num_times)
            tmp_data.append(data_file_name[i][17:-4])
            times_count.append('Term_' + str(num_times))
    data_file = pd.DataFrame(times_list, index=nameCount)

    return data_file


def Merge_Data(startNum, endNum, type_file):
    outputPath = '../data/processed/' + 'Merged' + str(startNum) + '-' + str(endNum) + '_' + type_file + '.csv'
    data_t = []
    for i in range(startNum, endNum + 1):
        timesName = '-' + str(i) + '_'
        fileName = '../data/raw/Engagement of Cyber Serurity/dataset201819/cyber-security' + timesName + type_file + '.csv'
        data = pd.read_csv(fileName)
        data_t.append(data)

    mergedData = pd.concat(data_t)
    print(mergedData.shape)
    mergedData.head()
    mergedData.to_csv(outputPath)

    return mergedData