import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('res.csv',delimiter=';')

fig0_o=plt.figure('minCapacity=0 and optimal')
probability=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==0)]['PROBABILITY']
time=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==0)]['TIME(s)']
#plt.scatter(probability,time, alpha=0.5)
sns.lineplot(x=probability,y=time)
plt.title('minCapacity=0 and optimal')
plt.xlabel('Percentual edge')
plt.ylabel('Time(s)')
fig0_o.savefig('Grafici/minCapacity=0 and optimal.png')

fig1_o=plt.figure('minCapacity=1 and optimal')
probability=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1)]['PROBABILITY']
time=data[(data['TERMINATION CONDITION']=='optimal') & (data['MINCAPACITY']==1)]['TIME(s)']
#plt.scatter(probability,time, alpha=0.5)
sns.lineplot(x=probability,y=time)
plt.title('minCapacity=1 and optimal')
plt.xlabel('Percentual edge')
plt.ylabel('Time(s)')
fig1_o.savefig('Grafici/minCapacity=1 and optimal.png')

fig2_o=plt.figure('minCapacity=2 and optimal')
probability=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='optimal')]['PROBABILITY']
time=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='optimal')]['TIME(s)']
#plt.scatter(probability,time, alpha=0.5)
sns.lineplot(x=probability,y=time)
plt.title('minCapacity=2 and optimal')
plt.xlabel('Percentual edge')
plt.ylabel('Time(s)')
fig2_o.savefig('Grafici/minCapacity=2 and optimal.png')

fig0_i=plt.figure('minCapacity=0 and infeasible')
probability=data[(data['MINCAPACITY']==0) & (data['TERMINATION CONDITION']=='infeasible')]['PROBABILITY']
time=data[(data['MINCAPACITY']==0) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)']
#plt.scatter(probability,time, alpha=0.5)
sns.lineplot(x=probability,y=time)
plt.title('minCapacity=0 and infeasible')
plt.xlabel('Percentual edge')
plt.ylabel('Time(s)')
fig0_i.savefig('Grafici/minCapacity=0 and infeasible')

fig1_i=plt.figure('minCapacity=1 and infeasible')
probability=data[(data['MINCAPACITY']==1) & (data['TERMINATION CONDITION']=='infeasible')]['PROBABILITY']
time=data[(data['MINCAPACITY']==1) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)']
#plt.scatter(probability,time, alpha=0.5)
sns.lineplot(x=probability,y=time)
plt.title('minCapacity=1 and infeasible')
plt.xlabel('Percentual edge')
plt.ylabel('Time(s)')
fig1_i.savefig('Grafici/minCapacity=1 and infeasible.png')

fig2_i=plt.figure('minCapacity=2 and infeasible')
probability=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='infeasible')]['PROBABILITY']
time=data[(data['MINCAPACITY']==2) & (data['TERMINATION CONDITION']=='infeasible')]['TIME(s)']
#plt.scatter(probability,time, alpha=0.5)
sns.lineplot(x=probability,y=time)
plt.title('minCapacity=2 and infeasible')
plt.xlabel('Percentual edge')
plt.ylabel('Time(s)')
fig2_i.savefig('Grafici/minCapacity=2 and infeasible.png')

hist=plt.figure("Histogram optimal/infeasibile")
terminationCondition=data['TERMINATION CONDITION']
plt.hist(terminationCondition, bins=2, rwidth=0.9)
hist.savefig('Grafici/histogram.png')

pie=plt.figure("Pie optimal/infeasibile")
number=[]
number.append(len(data[data['TERMINATION CONDITION']=='optimal']))
number.append(len(data[data['TERMINATION CONDITION']=='infeasible']))
plt.pie(number, labels=['optimal','infeasible'], startangle=90, explode=[0.1,0])
pie.savefig('Grafici/pie.png')

minc_o=plt.figure("mincapacity=2 vs mincapacity=1 vs mincapacity=0 for optimal")
minCapacityTime=data[data['TERMINATION CONDITION']=='optimal']['TIME(s)']
minCapacity=data[data['TERMINATION CONDITION']=='optimal']['MINCAPACITY']
sns.lineplot(x=minCapacity,y=minCapacityTime)
plt.title('mincapacity=2 vs mincapacity=1 vs mincapacity=0 for optimal')
plt.ylabel('Time(s)')
plt.xlabel('Variation Capacity')
minc_o.savefig('Grafici/mincapacity=2 vs mincapacity=1 vs mincapacity=0 for optimal.png')

fig7=plt.figure("mincapacity=2 vs mincapacity=1 vs mincapacity=0 for infeasible")
minCapacityTime=data[data['TERMINATION CONDITION']=='infeasible']['TIME(s)']
minCapacity=data[data['TERMINATION CONDITION']=='infeasible']['MINCAPACITY']
sns.lineplot(x=minCapacity,y=minCapacityTime)
plt.title('mincapacity=2 vs mincapacity=1 vs mincapacity=0 for infeasible')
plt.ylabel('Time(s)')
plt.xlabel('Variation Capacity')
fig7.savefig('Grafici/mincapacity=2 vs mincapacity=1 vs mincapacity=0 for infeasible.png')

fig8=plt.figure("Alcuin number")
probability1=list(data[(data['TERMINATION CONDITION']=='infeasible') & (data['MINCAPACITY']==1)]['PROBABILITY'].__array__())
capacity1=list(data[(data['TERMINATION CONDITION']=='infeasible') & (data['MINCAPACITY']==1)]['CAPACITY'].__array__())
probability2=list(data[(data['TERMINATION CONDITION']=='infeasible') & (data['MINCAPACITY']==2)]['PROBABILITY'].__array__())
capacity2=list(data[(data['TERMINATION CONDITION']=='infeasible') & (data['MINCAPACITY']==2)]['CAPACITY'].__array__())
graph1=data[(data['TERMINATION CONDITION']=='infeasible') & (data['MINCAPACITY']==1)]['GRAPH'].__array__()
print(type(graph1))
graph2=data[(data['TERMINATION CONDITION']=='infeasible') & (data['MINCAPACITY']==2)]['GRAPH'].__array__()
toremove=[]
for i in range(0, len(graph1)):
    for j in range(0,len(graph2)):
        if graph1[i][0:13]==graph2[j][0:13] and graph1[i][14::]==graph2[j][14::]:
            toremove.append(j)
            print(graph1[i]+"......"+graph2[j])
toremove=list(dict.fromkeys(toremove))
print(toremove)
for k in toremove[::-1]:
    probability2.pop(k)
    capacity2.pop(k)
capacity=capacity1+capacity2
capacity = [x+1 for x in capacity]
print(np.mean(capacity))
probability=probability1+probability2
sns.lineplot(x=probability, y=capacity)
plt.title("Alcuin number")
plt.xlabel("Percentual edge")
plt.ylabel("Alcuin number")
fig8.savefig("Grafici/Alcuin number.png")
