import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

data=pd.read_csv('res.csv',delimiter=';')
# popt, pcov = curve_fit(lambda t, a, b: a * np.exp(b * t), probability, time)
# # Extract the optimised parameters
# a = popt[0]
# b = popt[1]
# x_fitted_curve_fit = np.linspace(np.min(probability), np.max(time), 100)
# y_fitted_curve_fit = a * np.exp(b * x_fitted_curve_fit)
# fig1=plt.figure('1')
# plt.plot(x_fitted_curve_fit, y_fitted_curve_fit)
# plt.title('mincapacity=2 & termination condition infeasibile')
# print(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1)])
# probability=[0.9,0.8,0.7,0.6,0.5,0.4]
# time=[
#     np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==90)]['TIME(s)']),
#     np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==80)]['TIME(s)']),
#     np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==70)]['TIME(s)']),
#     np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==60)]['TIME(s)']),
#     np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==50)]['TIME(s)']),
#     np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==40)]['TIME(s)']),]
#fig1=plt.figure('1')
probability=data[data['MINCAPACITY']==1]['PROBABILITY']
time=data[data['MINCAPACITY']==1]['TIME(s)']
plt.scatter(probability,time)

#plt.plot(probability,time)
sns.lineplot(x=probability,y=time)
plt.show()