# AlcuinProblem
This project has the goal to study how much time is necessary to find if the generalization of Alcuin river crossing problem is feasible for a given graph and for a given number. To do this there are many parts:
- The model definition and resolver(requires CPLEX and pyomo python package)
- The graph generator(requires networkx python package)
- A file that convert the output from the graph generator to a dat file that can be used as input for the MIP resolver
- A file that execute the model for all the graphs
- A file that create SLURM file for all the graphs
- A file for elaboration of the result(requires numpy, matplotlib, seaborn, pandas)
- A simple example of river crossing problem(LPC) with the definition of concrete and abstract model

# Requires
- Python version 3.9
- Numpy version 1.24.2
- Pyomo version 6.5.0
- CPLEX(version 22.1.1) and his python bindings
- Networkx version 3.1
- Matplotlib version 3.7.1
- Seaborn version 0.12.2
- Pandas version 2.0.1
