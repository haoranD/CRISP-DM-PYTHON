import numpy as np
import pandas as pd
import sklearn
import csv
from os import listdir

def check_files(data_file_name):
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