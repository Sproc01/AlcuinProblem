import networkx as nx

#Il metodo di NetworkX utilizzato nella generazione di questa tipologia di grafi e' 
#gnprandomgraph(n,p,seed), che restituisce un’istanza di grafo G(n,p) di dimensione n in cui gli archi 
#hanno probabilita` di essere generati pari a p, mentre il parametro seed regola il comportamento 
#pseudo-casuale, in modo tale da permettere la riproducibilita` degli esperimenti.
i=0.1
while i<1:
    G1=nx.gnp_random_graph(50,i)
    nx.write_adjlist(G1, "GrafiCasuali/Graph"+str(i)+".txt")
    #capacita' barca: nx.approximation.maximum_independent_set(G1) Returns an approximate maximum independent set.
    c=len(G1)-len(nx.approximation.maximum_independent_set(G1))
    #scrivo valore su file
    file=open("GrafiCasuali/Graph"+str(i)+".txt","a")
    file.write("\n!"+str(c))
    file.close()
    i+=0.1