import networkx as nx

G1=nx.gnp_random_graph(100,0.3)
nx.write_adjlist(G1, "Grafi/gnp_random.txt")

G2=nx.random_regular_graph(10, 100)
nx.write_adjlist(G2, "Grafi/random_regular.txt")

G3=nx.watts_strogatz_graph(100, 10, 0.4)
nx.write_adjlist(G3, "Grafi/watts_strogatz.txt")

G4=nx.barabasi_albert_graph(100, 10)
nx.write_adjlist(G4, "Grafi/barbasi_albert.txt")

G5=nx.barabasi_albert_graph(10,4)
nx.write_adjlist(G5, "Grafi/prova.txt")
