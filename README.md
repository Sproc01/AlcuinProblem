# AlcuinProblem
This project has the goal to study how much time is necessary to find if the generalization of Alcuin river crossing problem is feasible for a given graph and for a given number. This project comprehends different parts:
- The model definition and resolver (requires CPLEX and Pyomo Python package)
- The graph generator (requires Networkx Python package)
- A file that convert the output from the graph generator to a dat file that can be used as input for the MIP resolver
- A file that execute the model for all the graphs with CPLEX seed=0
- A file that create SLURM file for all the graphs, each graph has 6 SLURM files because each graph must be resolved with 6 different CPLEX seed
- A file for elaboration of the result (requires some Python package: Numpy, Matplotlib, Seaborn, Pandas)
- A simple example of river crossing problem (graph: L-P-C) with the definition of a concrete and an abstract model

This program also shows some graphs about the time and one about the Alcuin Number of a graph highlighting the dependence between this number and the density of the graph.

This study is the center of my bachelor's degree thesis at University of Padua.

# Requires
- Python version 3.9
- Numpy version 1.24.2
- Pyomo version 6.5.0
- CPLEX version 22.1.1 and his Python bindings
- Networkx version 3.1
- Matplotlib version 3.7.1
- Seaborn version 0.12.2
- Pandas version 2.0.1
