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
from IPython.display import display
from time import time
import os
import sys

def files(data_file_name):
    num_times = 1
    times_list = []
    times_count = []
    tmp_data = []
    length_each = []
    just_count = 0

    for i in range(len(data_file_name)):

        if int(data_file_name[i][15]) != num_times:
            length_each.append(i - just_count)
            num_times += 1
            times_list.append(tmp_data)
            tmp_data = []
            just_count = i

        tmp_data.append(data_file_name[i][17:-4])
        times_count.append('Time_' + str(num_times))

    return times_list, times_count, length_each

def Get_Location():

    return


def dataFile_Merge(startNum, endNum,type_file):

    outputPath = '../data/processed/' + 'Merged' + str(startNum) + '-' + str(endNum) + '_' + type_file + '.csv'
    data_t = []
    for i in range(startNum, endNum + 1):
        print(i)
        timesName = '-' + str(i) + '_'
        fileName = '../data/raw/Engagement of Cyber Serurity/dataset201819/cyber-security' + timesName + type_file + '.csv'
        data = pd.read_csv(fileName)
        data_t.append(data)

    mergedData = pd.concat(data_t)
    mergedData.to_csv(outputPath)

    return mergedData