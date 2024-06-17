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
df1 = pd.read_csv('finished_measurements_3/st_commands.csv',names=headers)
df2 = pd.read_csv('finished_measurements_3/st_states.csv',names=headers)
plt.figure(1)
time = np.array(pd.to_numeric(df1['time_s'], errors='coerce') + pd.to_numeric(df1['time_ns'], errors='coerce') * 1e-9 )
#- df1['time_s'][0] - df1['time_ns'][0] * 1e-9)
velocity1 = np.array(pd.to_numeric(df1['velocity1'], errors='coerce'))
plt.plot(time,velocity1)
time = np.array(pd.to_numeric(df2['time_s'], errors='coerce') + pd.to_numeric(df2['time_ns'], errors='coerce') * 1e-9 )
#- df1['time_s'][0] - df1['time_ns'][0] * 1e-9
velocity1 = np.array(df2['velocity1'])
plt.plot(time,velocity1)
plt.title("SuperTwisting real velocity vs contol velocity")
df1 = pd.read_csv('pid_commands.csv',names=headers)
df2 = pd.read_csv('pid_states.csv',names=headers)
plt.figure(2)
time = np.array(pd.to_numeric(df1['time_s'], errors='coerce') + pd.to_numeric(df1['time_ns'], errors='coerce') * 1e-9 )#- df1['time_s'][0])
velocity1 = np.array(pd.to_numeric(df1['velocity1'], errors='coerce'))
plt.plot(time,velocity1)
time = np.array(pd.to_numeric(df2['time_s'], errors='coerce') + pd.to_numeric(df2['time_ns'], errors='coerce') * 1e-9 )#- df2['time_s'][0])
velocity1 = np.array(df2['velocity1'])
plt.plot(time,velocity1)
plt.title("PID real velocity vs contol velocity")
plt.show()
#print (time)