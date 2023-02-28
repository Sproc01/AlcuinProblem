from pyomo.environ import *
from pyomo.opt import SolverFactory

Places=["s","b","d"]
Nodes=["L","P","C"]
Trips=[]
Edges=["LP","PC"]
c=1

for j in range(2*len(Nodes)+1):
    Trips.append(j)

def obj_rule(model):
    return sum(model.y[f] for f in model.Trip)-1

def constr_rule1(model):
    return sum(model.x[i,"s",0] for i in model.Nodes)==model.Nodes.size()

def constr_rule2(model):
    return sum(model.x[i,"d",2*len(model.Nodes)+1] for i in model.Nodes)+sum(model.x[i,"b", 2*len(model.Nodes)+1] for i in model.Nodes)==model.Nodes.size()

def constr_rule3(model):
    return model.y[0]==1

def constr_rule4(model, i, f):
    return sum(model.x[i,l,f] for l in model.Places)==1

def constr_rule5(model, f):
    return model.y[f]<=model.y[f-1]

def constr_rule6(model, f):
    return sum(model.x[i,"s",f] for i in model.Nodes)+sum(model.x[i,"b",f] for i in model.Nodes)>=model.y[f]

def constr_rule7(model, f):
    return sum(model.x[i,"s",f] for i in model.Nodes)+sum(model.x[i,"b",f] for i in model.Nodes)<=len(model.Nodes)*model.y[f]

def constr_rule8(model, f):
    return sum(model.x[i,"b",f] for i in model.Nodes)<=model.Capacity*model.y[f]

def constr_rule9(model, f, i):
    if f%2==0:
        return model.x[i,"s",f]+model.x[i, "b", f]<=model.x[i,"s",f+1]+model.x[i, "b", f+1]
    else:
        return Constraint.Skip

def constr_rule10(model, f, i):
    if f%2!=0:
        return model.x[i,"d",f]+model.x[i, "b", f]<=model.x[i,"d",f+1]+model.x[i, "b", f+1]
    else:
        return Constraint.Skip

def constr_rule11(model, f, i):
    return model.x[i[0],"s",f]+model.x[i[1], "s", f]<=1

def constr_rule12(model, f, i):
    return model.x[i[0],"d",f]+model.x[i[1], "d", f]<=2-y[f]
	
def buildmodel():
    model=ConcreteModel()
    model.Places = Param(model.Items, initialize=lambda model, j: Places[j])
    model.Trips = Param(model.Items, initialize=lambda model, j: Trips[j])
    model.Edges = Param(model.Items, initialize=lambda model, j: Edges[j])
    model.Capacity = Param(mutable=False)
    model.Capacity.value = c
    # variables
    model.x = Var(model.Nodes, model.Places,model.Trip, domain=Boolean)
    model.y=Var(model.Trip, domain=Boolean)
    # objective
    model.obj = Objective(rule=obj_rule, sense=maximize)
    # constraints
    model.constrs1 = Constraint(rule=constr_rule1)
    model.constrs2 = Constraint(rule=constr_rule2)
    model.constrs3 =  Constraint(rule=constr_rule3)
    model.constrs4 =  Constraint(model.Nodes, model.Trips, rule=constr_rule4)
    model.constrs5 =  Constraint(model.Trips,rule=constr_rule5)
    model.constrs6 =  Constraint(model.Trips,rule=constr_rule6)
    model.constrs7 =  Constraint(model.Trips,rule=constr_rule7)
    model.constrs8 =  Constraint(model.Trips,rule=constr_rule8)
    model.constrs9 =  Constraint(model.Trips,rule=constr_rule9)#sistema
    model.constrs10 =  Constraint(model.Trips,rule=constr_rule10)#sistema
    model.constrs11 =  Constraint(model.Trips,rule=constr_rule11)
    model.constrs12 =  Constraint(model.Trips,rule=constr_rule12)
    return model

if __name__ == '__main__':
    import sys
    model = buildmodel()
    opt = SolverFactory('cplex_persistent')
    #instance = model.create_instance(sys.argv[1])
    #opt.set_instance(instance)
    res = opt.solve(tee=True)
    for p in instance.x:
	    print("x[{}] = {}".format(p, value(instance.x[p])))