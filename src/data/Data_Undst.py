import numpy as np
import squarify
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import plotly 
plotly.tools.set_credentials_file(username='haoran88', api_key='o8i3aa8qgpoIpCOBQgt8')
import pandas as pd
import sklearn
from os import listdir
import os
import sys
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import gmaps
import gmaps.datasets
from time import time

#Input the raw data with definition of type on data name.
#Output the unduplicate name of data----each kind  of data
def All_Kinds_Data(data_file_Path):
    #Store the number of term
    num_times = 1
    #Store all kinds of data in Term_n
    times_list = []
    times_count = []
    tmp_data = []
    length_each = []
    #for the table show
    nameCount = []
    just_count = 0

    for i in range(len(data_file_Path) + 1):
        if i >= len(data_file_Path):
            times_list.append(tmp_data)
            nameCount.append('Term_'+str(num_times))
        else:
            if int(data_file_Path[i][15]) != num_times:
                length_each.append(i - just_count)
                nameCount.append('Term_'+str(num_times))
                num_times += 1
                times_list.append(tmp_data)
                tmp_data = []
                just_count = i
            tmp_data.append(data_file_Path[i][17:-4])
            times_count.append('Term_'+str(num_times))
    #transform to be a dataframe to show easily
    data_file = pd.DataFrame(times_list,index=nameCount)
    return data_file


#Load the single file and show the 6 head of data
#parameters:
#           tNum : which term we want to load
#           type_file : which kind of data we want to load
def Load_single_file(tNum, type_file):
    data_t = []
    timesName = '-' + str(tNum) + '_'
    fileName = '../Data/raw/Engagement of Cyber Serurity/dataset201819/cyber-security' + timesName + type_file + '.csv'
    data = pd.read_csv(fileName)

    singlefile = pd.read_csv(fileName)

    return singlefile
