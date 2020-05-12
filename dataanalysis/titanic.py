
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')


data=pd.read_csv('C:/train.csv')
data.head()

sns.countplot('Pclass',data=data);
plt.show()