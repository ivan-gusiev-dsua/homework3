import pandas as pd
import seaborn as sns

# read file
doc = pd.read_csv('data/data.csv', sep='|', index_col=0, names=['date', 'link', 'text'], parse_dates=[0])

# group by day
group = doc.groupby(pd.TimeGrouper(freq='D'))
group = group.agg({'link':'count'})
