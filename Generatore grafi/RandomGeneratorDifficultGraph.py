import networkx as nx

z=0
k=100
p=[0.2,0.3,0.6,0.9]
seed=[10,60,200]
while z<3:
    for i in p:
        for j in seed:
            G1=nx.gnp_random_graph(k,i,seed=j)
            filename='GrafiCasuali/Graph'+str(int(i*100))+'_'+'_'+str(z)+'_'+str(j)+'.txt'
            nx.write_adjlist(G1,filename)
            #capacita' barca: nx.approximation.maximum_independent_set(G1) Returns an approximate maximum independent set.
            c=len(G1)-len(nx.approximation.maximum_independent_set(G1))-z
            #scrivo valore su file
            file=open(filename,"a")
            file.write("\n!"+str(c))
            file.close()
    z+=1