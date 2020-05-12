# Setup

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np


# import folium
# import plotly.express as px
# import plotly.graph_objects as go

# for time series
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
#import plotly.offline as py

# py.init_notebook_mode()
pd.plotting.register_matplotlib_converters()
sns.set_style("whitegrid")
pd.set_option("display.max_columns",30)

# load data
patient = pd.read_csv("C:/inputcsv/covid/patient.csv", index_col ="patient_id")
time = pd.read_csv("C:/inputcsv/covid/time.csv", index_col="date")
route = pd.read_csv("C:/inputcsv/covid/route.csv", index_col="patient_id")

patient.tail()
pd.DataFrame.count