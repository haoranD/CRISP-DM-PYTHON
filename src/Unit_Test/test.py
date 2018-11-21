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
import unittest
sys.path.append('..')
from data.Data_Undst import *
from data.Data_Preparation import *

def test_AKD_False():
        assert type(All_Kinds_Data(3)) == pd.DataFrame


def test_LSF_False():
        assert type(Load_single_file('fs', 9)) == pd.DataFrame
def test_LSF_False2():
        assert type(Load_single_file(98, 'question-response')) == pd.DataFrame


def test_MD_False():
        assert type(Merge_Data(9, 1, 'enrolments')) == pd.DataFrame


def test_ED_False():
        assert type(extract_data('question-response',' correct',term = 5, ifMerged = True, start_term=2, end_term=1)) == pd.DataFrame

