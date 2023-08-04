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

fig0_o=plt.figure('minCapacity=0 and optimal')
probability=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==0)]['PROBABILITY']
time=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==0)]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig0_o.savefig('../Grafici/minCapacity=0 and optimal.png')

fig0_i=plt.figure('minCapacity=0 and infeasible')
probability=data[(data['MINCAPACITY']==0) & (data['TERMINATION CONDITION']=='infeasible')]['PROBABILITY']
time=data[(data['MINCAPACITY']==0) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig0_i.savefig('../Grafici/minCapacity=0 and infeasible.png')

fig1_o=plt.figure('minCapacity=1 and optimal')
probability=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1)]['PROBABILITY']
time=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1)]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig1_o.savefig('../Grafici/minCapacity=1 and optimal.png')

fig1_i=plt.figure('minCapacity=1 and infeasible')
probability=data[(data['MINCAPACITY']==1) & (data['TERMINATION CONDITION']=='infeasible')]['PROBABILITY']
time=data[(data['MINCAPACITY']==1) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig1_i.savefig('../Grafici/minCapacity=1 and infeasible.png')

fig2_i=plt.figure('minCapacity=2 and infeasible')
probability=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='infeasible')]['PROBABILITY']
time=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig2_i.savefig('../Grafici/minCapacity=2 and infeasible.png')

fig2_o=plt.figure('minCapacity=2 and optimal')
probability=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='optimal')]['PROBABILITY']
time=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='optimal')]['TIME(s)']
plt.scatter(probability,time)
sns.lineplot(x=probability,y=time)
fig2_o.savefig('../Grafici/minCapacity=2 and optimal.png')

hist=plt.figure("Histogram optimal/infeasibile")
terminationCondition=data['TERMINATION CONDITION']
plt.hist(terminationCondition, bins=2, rwidth=0.9)
hist.savefig('../Grafici/histogram.png')

minc_o=plt.figure("mincapacity=2 vs mincapacity=1 vs mincapacity=0 for optimal")
minCapacityTime=data[data['TERMINATION CONDITION']=='optimal']['TIME(s)']
minCapacity=data[data['TERMINATION CONDITION']=='optimal']['MINCAPACITY']
plt.scatter(minCapacity, minCapacityTime)
minCapacityTime1avg=np.mean(data[(data['MINCAPACITY']==1) & (data['TERMINATION CONDITION']=='optimal')]['TIME(s)'])
minCapacityTime2avg=np.mean(data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='optimal')]['TIME(s)'])
minCapacityTime0avg=np.mean(data[(data['MINCAPACITY']==0) & (data['TERMINATION CONDITION']=='optimal')]['TIME(s)'])
plt.scatter([0,1,2],[minCapacityTime0avg,minCapacityTime1avg,minCapacityTime2avg])
minc_o.savefig('../Grafici/mincapacity=2 vs mincapacity=1 vs mincapacity=0 for optimal.png')

fig7=plt.figure("mincapacity=2 vs mincapacity=1 vs mincapacity=0 for infeasible")
minCapacityTime=data[data['TERMINATION CONDITION']=='infeasible']['TIME(s)']
minCapacity=data[data['TERMINATION CONDITION']=='infeasible']['MINCAPACITY']
plt.scatter(minCapacity, minCapacityTime)
minCapacityTime1avg=np.mean(data[(data['MINCAPACITY']==1) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)'])
minCapacityTime2avg=np.mean(data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)'])
minCapacityTime0avg=np.mean(data[(data['MINCAPACITY']==0) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)'])
plt.scatter([0,1,2],[minCapacityTime0avg,minCapacityTime1avg,minCapacityTime2avg])
fig7.savefig('../Grafici/mincapacity=2 vs mincapacity=1 vs mincapacity=0 for infeasible.png')

#plt.show()