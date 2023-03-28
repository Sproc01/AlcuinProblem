import networkx as nx

#Il metodo di NetworkX utilizzato nella generazione di questa tipologia di grafi e' gnprandomgraph(n,p,seed), che restituisce un’istanza di grafo G(n,p) di dimen- sione n in cui gli archi hanno probabilita` di essere generati pari a p, mentre il parametro seed regola il comportamento pseudo-casuale, in modo tale da permettere la riproduci- bilita` degli esperimenti.
G1=nx.gnp_random_graph(100,0.1)
nx.write_adjlist(G1, "Grafi/gnp_random.txt")

#Il metodo di NetworkX utilizzato nella generazione di questa tipologia di grafi e' random regular graph(d, n, seed), che restituisce un’istanza di grafo regolare di di- mensione n in cui tutti i nodi hanno grado d. Il parametro seed anche in questo caso regola il comportamento pseudo-casuale della generazione, permettendo la replicabilit`a dell’esperimento.
G2=nx.random_regular_graph(10, 100)
nx.write_adjlist(G2, "Grafi/random_regular.txt")

#Il metodo di NetworkX utilizzato nella generazione di questa tipologia di grafi e' watts strogatz graph(n, k, p, seed), che restituisce un’istanza di grafo di Watts- Strogatz di dimensione n. I nodi di questo grafo sono inizialmente organizzati in una struttura ad anello in cui ogni nodo `e collegato ai suoi k//2+1 vicini sinistri e k//2+1 vicini destri ed in cui la probabilit`a che ciascun nodo sia ”ricollegato” con un altro nodo diverso da uno dei suoi vicini attuali `e p. Anche in questo caso il parametro seed regola il comportamento casuale della generazione, permettendo cosi' di ottenere la riproducibilita` dei risultati.
G3=nx.watts_strogatz_graph(100, 10, 0.1)
nx.write_adjlist(G3, "Grafi/watts_strogatz.txt")

#Il metodo di NetworkX utilizzato nella generazione di questa tipologia di grafi e' barabasi albert graph(n, m, seed), che restituisce un’istanza di grafo Barabasi-Albert di dimensione n in cui ogni nuovo nodo viene collegato nel procedimento iterativo a m nodi esistenti. Anche in questo caso il parametro seed regola il comportamento casuale del- la generazione, agendo in particolare sulla scelta dell’insieme di archi da creare ad ogni iterazione, permettendo cosi' la replicabilit`a dell’esperimento.
G4=nx.barabasi_albert_graph(100, 10)
nx.write_adjlist(G4, "Grafi/barbasi_albert.txt")

#grafo prova con pochi elementi
G5=nx.barabasi_albert_graph(10,4)
nx.write_adjlist(G5, "Grafi/prova.txt")
