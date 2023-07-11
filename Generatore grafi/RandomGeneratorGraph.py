import networkx as nx

#Il metodo di NetworkX utilizzato nella generazione di questa tipologia di grafi e' 
#gnprandomgraph(n,p,seed), che restituisce un’istanza di grafo G(n,p) di dimensione n in cui gli archi 
#hanno probabilita` di essere generati pari a p, mentre il parametro seed regola il comportamento 
#pseudo-casuale, in modo tale da permettere la riproducibilita` degli esperimenti.
k=50
while k<=150:
    i=0.1
    while i<=0.9:
        G1=nx.gnp_random_graph(k,i,1)
        nx.write_adjlist(G1, "GrafiCasuali/Graph"+str(i)+'_'+str(k)+".txt")
        #capacita' barca: nx.approximation.maximum_independent_set(G1) Returns an approximate maximum independent set.
        c=len(G1)-len(nx.approximation.maximum_independent_set(G1))
        #scrivo valore su file
        file=open("GrafiCasuali/Graph"+str(i)+'_'+str(k)+".txt","a")
        file.write("\n!"+str(c))
        file.close()
        i+=0.1
    k+=50


#Il metodo di NetworkX utilizzato nella generazione di questa tipologia di grafi e' 
#random regular graph(d, n, seed), che restituisce un’istanza di grafo regolare di dimensione n 
#in cui tutti i nodi hanno grado d. Il parametro seed anche in questo caso regola il
#comportamento pseudo-casuale della generazione, permettendo la replicabilita' dell’esperimento.
#i=1
#while i<10:
    #G1=nx.random_regular_graph(i, 100)
    #nx.write_adjlist(G1, "GrafiCasuali/Graph"+str(i)+".txt")
    #capacita' barca: nx.approximation.maximum_independent_set(G1) Returns an approximate maximum independent set.
    #c=len(G1)-len(nx.approximation.maximum_independent_set(G1))
    #scrivo valore su file
    #file=open("GrafiCasuali/Graph"+str(i)+".txt","a")
    #file.write("\n!"+str(c))
    #file.close()
    #i+=1