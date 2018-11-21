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
from SimpleTest import SimpleUnittestTest
import unittest

if __name__ == '__main__':

    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromNames(['SimpleTest.SimpleUnittestTest']))

    with open('SimpleUnittest.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)