from src import *
import numpy as np
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import plotly 
import pandas as pd
plotly.tools.set_credentials_file(username='haoran88', api_key='o8i3aa8qgpoIpCOBQgt8')
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

#Merge data from bottom row of first data
#Output the Merged data
#Parameter:
#         startNum : first data
#         endNum :  last data
#         type_file : which kind of data will be merged
def Merge_Data(startNum, endNum, type_file):
    outputPath = '../Data/processed/' + 'Merged' + str(startNum) + '-' + str(endNum) + '_' + type_file + '.csv'
    data_t = []
    
    #Store from startNum data to endNum data
    for i in range(startNum,endNum+1):
        timesName = '-' + str(i) + '_'
        fileName = '../Data/raw/Engagement of Cyber Serurity/dataset201819/cyber-security' + timesName + type_file + '.csv'
        data = pd.read_csv(fileName)
        data_t.append(data)

    #Merge them
    mergedData = pd.concat(data_t)
    mergedData.to_csv(outputPath)
    print('Successfully Combined')

    return mergedData

#Get certain locations for each country
#Output the lattitude and longitude
#
def Get_Loc():
    data = pd.read_csv('../data/processed/' +'Detected_Country' + '_157' + '.csv')
    lat = []
    lon = []
    count = 0
    
    #loop for searching location in google map
    for i in data['Country']:
        geolocator = Nominatim(user_agent="nnccll")
        location = geolocator.geocode(str(i))
        lat.append(str(location.latitude))
        lon.append(str(location.longitude))
        #in case to push to request
        sleep(60)
    
    locations = []
    for i in range(len(lat)):
        locations.append((lat[i],lon[i]))
    lcts = pd.DataFrame(locations)
    #Generates new file
    lcts.to_csv('../data/external/Country-locations.csv')

    return locs

#Use the new file generates in Get_LOC()
#Output the WHOLE certain locations for students
#
def all_loc():
    merged_enrolment = pd.read_csv('../Data/processed/Merged3-7_enrolments.csv' )
    locs = pd.read_csv('../Data/external/Country-locations.csv')
    country_locs = pd.read_csv('../Data/processed/Detected_Country_157.csv')
    country_locs = np.array(country_locs)
    country_locs = country_locs.tolist()
    tmp = []
    for i in country_locs:
        tmp.append(str(i[0]))
    
    #Find the location fix to whole country
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

#Input the column in which kind of data you want to extract
#Output to the ../Data/processed folder and return the new extracted file
#Parameter:
#         data_file_Path : main root of all single file
#         data_type : in which kind of data we want to extract : 
#         extract_name : which column you want to extract
#         term : from not merged data which term we interested in
#         ifMerged: flag for using merged data
#         start_term: if use merged data, this is the begaining number of it
#         end_term: if use merged data, this is the ending number of it
#
def extract_data(data_type, extract_name,term = 0, ifMerged = False, start_term=0, end_term=0):
    
    extract_col = []

    # Judge if we use the merged data
    if ifMerged:
        path  = '../Data/processed/Merged' + str(start_term) + '-' + str(end_term) + '_' + data_type +'.csv' 
        outputPath = '../Data/processed/Extracted' + str(start_term) + '-' + str(end_term) + '_' + data_type +'.csv' 

    else:
        path = '../Data/raw/Engagement of Cyber Serurity/dataset201819/cyber-security-' + str(term) + '_' + data_type + '.csv'
        outputPath = '../Data/processed/Extracted' + str(term) + '_' + data_type +'.csv' 

    data = pd.read_csv(path)

    # generates new file
    for i in extract_name:
        extract_col.append(data[i])
    
    exNew = pd.concat(extract_col,axis=1)

    exNew.to_csv(outputPath)
    
    return exNew