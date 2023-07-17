import networkx as nx

z=0
k=100
p=0.9
seed=0
while z<10:
    #while seed<40:
    G1=nx.gnp_random_graph(k,p,seed=seed)
    filename='GrafiCasuali/Graph'+str(int(p*100))+'_'+str(z)+'_'+str(seed)+'.txt'
    nx.write_adjlist(G1,filename)
    #capacita' barca: nx.approximation.maximum_independent_set(G1) Returns an approximate maximum independent set.
    c=len(G1)-len(nx.approximation.maximum_independent_set(G1))-z
    #scrivo valore su file
    file=open(filename,"a")
    file.write("\n!"+str(c))
    file.close()
    #seed+=1
    z+=1