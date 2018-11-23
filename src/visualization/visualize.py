from src import *
import numpy as np
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
from IPython.display import display
import plotly.plotly as py
import plotly.graph_objs as go
from time import time

#Preprocess and generates the necessary parameters for gender pie plot
#input the single file which gender variable in,it should be 'enrolment'
#
#
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


#Preprocess and generates the necessary parameters for bar plot
#input the single file which country variable in,it should be 'enrolment'
#
#
def country_bar(singlefile):
    singlefile = singlefile[singlefile['detected_country'] != 'Unknown']
    country = singlefile['detected_country']

    re = pd.value_counts(country)

    re_vale = re.tolist()[0:20]
    re_name = re.index.tolist()[0:20]
    
    return re_name,re_vale



#Preprocess and generates the necessary parameters for  pie plot
#input the two files which country variable in,it should be 'enrolment'
#
#
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



#Preprocess and generates the necessary parameters for answer line plot
#input the single file which question variable in,it should be 'question-response'
#
#
def answer_line(singlefile):
    numF = len(singlefile[singlefile['correct'] == False])
    numT = len(singlefile[singlefile['correct'] == True])

    question = pd.unique(singlefile['quiz_question'])

    WrongAnswer_percent = []

    choose_tmp = singlefile[singlefile['correct'] == False]

    for i in question:
        WrongAnswer_percent.append(len(choose_tmp[choose_tmp['quiz_question'] == i]) / len(singlefile['quiz_question'] == i))

    return question, WrongAnswer


#Preprocess and generates the necessary parameters for treemap  plot
#input the single file which leaving reason variable in,it should be 'leaving rsponse survey'
#
#
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
