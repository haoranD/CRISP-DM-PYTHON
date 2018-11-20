from src import *
import numpy as np
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import plotly 
import pandas as pd
import sklearn
from os import listdir
import os
import sys
import csv
from IPython.display import display
import plotly.plotly as py
import plotly.graph_objs as go
from time import time

def gender_pie(singlefile):
    singlefile = singlefile[singlefile['gender'] != 'Unknown']

    print('The other genders are just occupy a very little,so we do not need to consider them temporarily')
    print('Proportions of the male and female tend to balance.')
    print('The differences between male and female we can asuume that male have more interests in this kind of course.')

    labels = ['Female','Male','Other']
    values = [float(len(singlefile[singlefile['gender'] == 'female'])) / float(len(singlefile['gender'])) ,
                float(len(singlefile[singlefile['gender'] == 'male'])) / float(len(singlefile['gender'])) ,
                float(len(singlefile[singlefile['gender'] == 'other'])) / float(len(singlefile['gender']))]

    return labels, values

def country_bar(singlefile):
    singlefile = singlefile[singlefile['detected_country'] != 'Unknown']
    country = singlefile['detected_country']

    re = pd.value_counts(country)

    re_vale = re.tolist()[0:20]
    re_name = re.index.tolist()[0:20]
    
    return re_name,re_vale


def country_pie(fileName1, fileName2):
    pie1 = fileName1
    pie1 = pie1[pie1['detected_country'] != 'Unknown']
    pie1 = pie1['detected_country']

    re = pd.value_counts(pie1)

    re_value1 = re.tolist()[0:20]
    re_name1 = re.index.tolist()[0:20]
    

    pie2 = fileName2
    pie2 = pie2[pie2['detected_country'] != 'Unknown']
    pie2 = pie2['detected_country']

    re = pd.value_counts(pie2)

    re_value2 = re.tolist()[0:20]
    re_name2 = re.index.tolist()[0:20]

    return re_name1,re_value1,re_name2,re_value2


def answer_line(singlefile):
    numF = len(singlefile[singlefile['correct'] == False])
    numT = len(singlefile[singlefile['correct'] == True])

    question = pd.unique(singlefile['quiz_question'])

    WrongAnswer = []

    choose_tmp = singlefile[singlefile['correct'] == False]

    for i in question:
        WrongAnswer.append(len(choose_tmp[choose_tmp['quiz_question'] == i]))

    return question, WrongAnswer

def Treemap(singlefile):
    reasons = pd.unique(singlefile['leaving_reason'])

    reasons = reasons.tolist()
    re_va = []

    for i in reasons:
        re_va.append(len(singlefile[singlefile['leaving_reason'] == i]))    
        dict_reasons = dict(zip(reasons,re_va))

    invalid_data = list(range(int((1/5) * max(re_va))))

    for i in reasons:
        if dict_reasons[i] in invalid_data:
            dict_reasons.pop(i)
        
    reasons = list(dict_reasons.keys())
    re_va = list(dict_reasons.values())

    return reasons, re_va


def Heatmap_Google():
    gmaps.configure(api_key="AIzaSyB2DKOMtZVdPBThMcJyWZhnyTvdrn_HuRo") # Your Google API key

    # load a Numpy array of (latitude, longitude) pairs
    #locations = gmaps.datasets.load_dataset("taxi_rides")
    print('Alomost half of students come from European,and many of others are from Asia and South America')
    print('Also, the proportions of the not english speaking country is big enough, and for the students better experien-ce, it is necessary to give some subtitles for these major area of students ')
    fig = gmaps.figure()

    fig.add_layer(gmaps.heatmap_layer(locations,max_intensity=20, point_radius=9.0))

    fig