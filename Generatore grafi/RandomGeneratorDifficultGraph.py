import networkx as nx
#Instanze difficili: (90,-1),(60,-2), (50,-2),(40,-2)
z=0#[1,2]
dim=100
p=[0.9,0.8,0.7,0.6,0.5,0.4]
seed=[7,17,41,43,79]
for i in p:
    for k in seed:
        G1=nx.gnp_random_graph(dim,i,seed=k)
        #for j in z:
        #capacita' barca: nx.approximation.maximum_independent_set(G1) Returns an approximate maximum independent set.
        c=len(G1)-len(nx.approximation.maximum_independent_set(G1))-z
        filename='GrafiCasuali/Graph'+str(int(i*100))+'_'+str(z)+'_'+str(k)+'.txt'
        nx.write_adjlist(G1,filename)
        #scrivo valore su file
        file=open(filename,"a")
        file.write("\n!"+str(c))
        file.close()