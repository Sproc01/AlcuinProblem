import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('res.csv',delimiter=';')
# fig0=plt.figure('minCapacity=1 and optimal avg time')
# probability=[0.9,0.8,0.7,0.6,0.5,0.4]
# time=[
#      np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==90)]['TIME(s)']),
#      np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==80)]['TIME(s)']),
#      np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==70)]['TIME(s)']),
#      np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==60)]['TIME(s)']),
#      np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==50)]['TIME(s)']),
#      np.mean(data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1) & (data['PROBABILITY']==40)]['TIME(s)']),]
# plt.scatter(probability,time)
# sns.lineplot(x=probability,y=time)

fig1=plt.figure('minCapacity=1 and optimal')
probability=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1)]['PROBABILITY']
time=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1)]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig1.savefig('../Grafici/minCapacity=1 and optimal.png')

fig3=plt.figure('minCapacity=1 and infeasible')
probability=data[(data['MINCAPACITY']==1) & (data['TERMINATION CONDITION']=='infeasible')]['PROBABILITY']
time=data[(data['MINCAPACITY']==1) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig3.savefig('../Grafici/minCapacity=1 and infeasible.png')

fig4=plt.figure('minCapacity=2 and infeasible')
probability=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='infeasible')]['PROBABILITY']
time=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig4.savefig('../Grafici/minCapacity=2 and infeasible.png')

fig5=plt.figure('minCapacity=2 and optimal')
probability=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='optimal')]['PROBABILITY']
time=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='optimal')]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig5.savefig('../Grafici/minCapacity=2 and optimal.png')

fig2=plt.figure("Histogram optimal/infeasibile")
terminationCondition=data['TERMINATION CONDITION']
plt.hist(terminationCondition, bins=2, rwidth=0.9)
fig2.savefig('../Grafici/histogram.png')

plt.show()