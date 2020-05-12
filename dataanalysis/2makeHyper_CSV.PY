import numpy as np
import pandas as pd
import os

base_file = 'C:/inputcsv/painting/conUNSOUNG/FAMILY(PAI, UN-SOUNG)/3. Material Analysis/3.3 Spectrum Analysis/3.3.3. VNIR(1000-1600nm) Spectrum'
files = os.listdir(base_file)



hyper_list = []


df_Hyper = pd.DataFrame(columns=['nm'])


for file in files:

    path = os.path.join(base_file,file)
    point = 0
    if 'VIR' in file:
        point = file[-20:-17]
    elif 'VNIR' in file:
        point = file[-21:-18]
  
    col_name = ['nm',point]

    # 공백을 구분자로한 csv 파일 읽기 # col_names 명시 
    data = pd.read_table(path,sep="\s+",names= col_name)
    df_Hyper = pd.merge(df_Hyper,data,how='outer',on='nm')

df_Hyper.set_index('nm')


import datetime
basename = os.getcwd()+'\\'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
df_Hyper.to_csv(basename+'HyperSpectrum.csv')

