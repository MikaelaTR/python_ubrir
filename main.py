import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import PySimpleGUI as sg
from datetime import datetime
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import PySimpleGUI as psg
import pylab
df = pd.read_csv('DataSet.csv')
df.head()
df['rep_date'] = df['rep_date'].apply(
    lambda x: datetime.strptime(x, '%m/%d/%Y'))
df["date_today"] = date.today()
df['date_today'] = pd.to_datetime(df['date_today'],  format = '%Y/%m/%d')
df["Recency"] =  \
(df["date_today"] - df["rep_date"]).dt.days
df = df.sort_values(by='partner ', ascending=True)
rfm = (df.pivot_table(index="partner ",
     values=["monetary","Recency"],
     aggfunc={"Recency": np.min, "monetary":[np.sum, len]},
     fill_value=0))
rfm["Av_sum"] = rfm['monetary', 'sum'] / rfm['monetary', 'len']
rfm.columns = ['recency', 'frequency', 'monetary', 'AVG_SUM']
rfm['R'] = pd.qcut(rfm['recency'],
                              q=3,
                              labels=[3,2,1])
rfm['F'] = pd.qcut(rfm['frequency'],
                              q=4,
                              labels=[1,2,3],duplicates = 'drop')
rfm['M'] = pd.qcut(rfm['AVG_SUM'],
                              q=3,
                              labels=[1,2,3],duplicates = 'drop')
rfm["RFM"] = rfm["R"].astype ( str ) + rfm["F"].astype ( str ) + rfm["M"].astype ( str )
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

layout = [[sg.Text('If you want to create charts, click <Build Graphs>',
                   font=('Arial Bold', 16),
                   size=20, expand_x=True,
                   justification='center')],
            [sg.Button('Build Graphs',
                       font=('Arial Bold', 16),
                       size=20, expand_x=True),
             sg.Button('Cancel',
                       font=('Arial Bold', 16),
                       size=20, expand_x=True)]]

# Create the Window
window = sg.Window('Program for calculating the RFM model', layout, size=(900,100), keep_on_top=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    fig = plt.figure(figsize=(20, 20), dpi=80, facecolor='w', edgecolor='k')
    plt.subplot(2, 2, 1)
    rfm.groupby('RFM').agg('frequency').mean().plot(kind='bar', color='#0000CC')
    plt.title('Соотношение частоты покупок и показателей RFM')
    plt.subplot(2, 2, 2)
    rfm.groupby('F').agg('frequency').mean().plot(kind='bar', color='#FF69B4')
    plt.title('Распределение клиентов по частоте покупок')
    plt.subplot(2, 2, 3)
    rfm.groupby('R').agg('recency').mean().plot(kind='bar', color='#9ACD32')
    plt.title('Распределение клиентов по дате последней покупки')
    plt.subplot(2, 2, 4)
    rfm.groupby('M').agg('AVG_SUM').mean().plot(kind='bar', color='#FFD700')
    plt.title('Распределение клиентов по среднему чеку')
    plt.show()

window.close()
