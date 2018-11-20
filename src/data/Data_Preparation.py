from src import *
import numpy as np
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import plotly 
import pandas as pd
plotly.tools.set_credentials_file(username='haoran88', api_key='pP3roY52YPNbI68oB3KS')
import sklearn
from os import listdir
import os
import squarify
import sys
import csv
from IPython.display import display
import plotly.plotly as py
import plotly.graph_objs as go
from time import time

def Merge_Data(startNum, endNum, type_file):
    outputPath = '../Data/processed/' + 'Merged' + str(startNum) + '-' + str(endNum) + '_' + type_file + '.csv'
    data_t = []
    for i in range(startNum,endNum+1):
        timesName = '-' + str(i) + '_'
        fileName = '../Data/raw/Engagement of Cyber Serurity/dataset201819/cyber-security' + timesName + type_file + '.csv'
        data = pd.read_csv(fileName)
        data_t.append(data)

    
    mergedData = pd.concat(data_t)
    mergedData.to_csv(outputPath)
    print('Successfully Combined')

    return mergedData

def Get_Loc():
    data = pd.read_csv('../data/processed/' +'Detected_Country' + '_157' + '.csv')
    lat = []
    lon = []
    count = 0
    for i in data['Country']:
        geolocator = Nominatim(user_agent="nnccll")
        location = geolocator.geocode(str(i))
        lat.append(str(location.latitude))
        lon.append(str(location.longitude))
        sleep(60)
    
    locations = []
    for i in range(len(lat)):
        locations.append((lat[i],lon[i]))
    lcts = pd.DataFrame(locations)
    lcts.to_csv('../data/external/Country-locations.csv')

    return locs

def all_loc():
    merged_enrolment = pd.read_csv('../Data/processed/Merged3-7_enrolments.csv' )
    locs = pd.read_csv('../Data/external/Country-locations.csv')
    country_locs = pd.read_csv('../Data/processed/Detected_Country_157.csv')
    country_locs = np.array(country_locs)
    country_locs = country_locs.tolist()
    tmp = []
    for i in country_locs:
        tmp.append(str(i[0]))
    
    locs = np.array(locs)
    locs = locs.tolist()
    locations = []
    for i in range(len(locs)):
        del locs[i][0]

    for i in merged_enrolment['detected_country']:
        if i not in tmp:
            pass
        else:
            locations.append(locs[tmp.index(i)])

    return locations

def extract_data(data_type, extract_name,term = 0, ifMerged = False, start_term=0, end_term=0):
    
    extract_col = []

    if ifMerged:
        path  = '../Data/processed/Merged' + str(start_term) + '-' + str(end_term) + '_' + data_type +'.csv' 
        outputPath = '../Data/processed/Extracted' + str(start_term) + '-' + str(end_term) + '_' + data_type +'.csv' 

    else:
        path = '../Data/raw/Engagement of Cyber Serurity/dataset201819/cyber-security-' + str(term) + '_' + data_type + '.csv'
        outputPath = '../Data/processed/Extracted' + str(term) + '_' + data_type +'.csv' 

    data = pd.read_csv(path)

    for i in extract_name:
        extract_col.append(data[i])
    
    exNew = pd.concat(extract_col,axis=1)

    exNew.to_csv(outputPath)
    
    return exNew

def clean_AllCountry():

    return cleaned_country