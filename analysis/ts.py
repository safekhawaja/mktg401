import pandas as pd
from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt

# Rolling averages

pre_evite = pd.read_csv("/Users/saif/Downloads/data_cleaned_for_class.csv", index_col=0, parse_dates=True)
pre_evite["date"] = pre_evite.apply(lambda x: datetime.strptime(x["date"][0:7], "%d%b%y"), axis=1)
pre_evite.sort_values(by='date')
pre_evite = pre_evite.groupby('date')['events'].sum().reset_index()

pre_evite_7 = pre_evite.assign(rm7=pre_evite.events.rolling(window=7).mean())
pre_evite_30 = pre_evite_7.assign(rm30=pre_evite.events.rolling(window=30).mean())
pre_evite_365 = pre_evite_30.assign(rm365=pre_evite.events.rolling(window=365).mean())

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(pre_evite.date, pre_evite_365.rm7, color='#444444', linestyle='-', label='7-Day Moving Average')
plt.plot(pre_evite.date, pre_evite_365.rm30, color='#444444', linestyle='--', label='30-Day Moving Average')
plt.plot(pre_evite.date, pre_evite_365.rm365, color='#444444', linestyle=':', label='365-Day Moving Average')
plt.legend()
plt.show()
