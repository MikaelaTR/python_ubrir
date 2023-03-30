import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
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
rfm.columns = ['Recency', 'Repeat', 'SUM', 'AVG_SUM']
rfm['R'] = pd.qcut(rfm['Recency'],
                              q=3,
                              labels=[3,2,1])
rfm['F'] = pd.qcut(rfm['Repeat'],
                              q=4,
                              labels=[1,2,3],duplicates = 'drop')
rfm['M'] = pd.qcut(rfm['AVG_SUM'],
                              q=3,
                              labels=[1,2,3],duplicates = 'drop')
rfm["RFM"] = rfm["R"].astype ( str ) + rfm["F"].astype ( str ) + rfm["M"].astype ( str )
print(rfm)