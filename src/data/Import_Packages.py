import numpy as np
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import squarify
import gmaps
import gmaps.datasets
import plotly 
plotly.tools.set_credentials_file(username='haoran88', api_key='vrWPoiiR7GpTYytENIAB')
import pandas as pd
import sklearn
from os import listdir
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from src.data import EDA,Data_Loader
import csv
from IPython.display import display
import plotly.plotly as py
import plotly.graph_objs as go

from time import time


print('Successfully import all the necessary packages')