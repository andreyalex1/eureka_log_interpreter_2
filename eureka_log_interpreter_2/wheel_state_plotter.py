import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
headers = ['time_s','time_ns','frame_id', 
'name1','name2','name3','name4','name5','name6',
'position1', 'position2', 'position3', 'position4', 'position5', 'position6',
'velocity1', 'velocity2', 'velocity3', 'velocity4', 'velocity5', 'velocity6', 
'effort1', 'effort2', 'effort3', 'effort4', 'effort5', 'effort6', ]
df = pd.read_csv('topic.csv',names=headers)
time = np.array(df['time_s'] + df['time_ns'] * 1e-9 - df['time_s'][0])
velocity1 = np.array(df['velocity1'])
plt.plot(time,velocity1)
plt.show()
#print (time)