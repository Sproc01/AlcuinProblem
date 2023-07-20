import networkx as nx
#Instanze difficili: (90,-1),(60,-2), (50,-2),(40,-2)
z=1
k=100
p=[0.9,0.6,0.5,0.4]
seed=0
for i in p:
    while seed<10:
        G1=nx.gnp_random_graph(k,i,seed=seed)
        filename='GrafiCasuali/Graph'+str(int(i*100))+'_'+str(z)+'_'+str(seed)+'.txt'
        nx.write_adjlist(G1,filename)
        #capacita' barca: nx.approximation.maximum_independent_set(G1) Returns an approximate maximum independent set.
        c=len(G1)-len(nx.approximation.maximum_independent_set(G1))-z
        #scrivo valore su file
        file=open(filename,"a")
        file.write("\n!"+str(c))
        file.close()
        seed+=1
    z=2
    seed=0