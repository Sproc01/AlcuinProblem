from pyomo.environ import *
from pyomo.opt import SolverFactory

Places=["s","b","d"]
Nodes=["L","P","C"]
Trips=[]
Edges=["LP","PC"]
c=1

for j in range(2*len(Nodes)+2):
    Trips.append(j)

def obj_rule(model):
    return sum(model.y[f] for f in model.Trips)-1

def constr_rule1(model):
    return sum(model.x[i,"s",0] for i in model.Nodes)==len(model.Nodes)

def constr_rule2(model):
    return sum(model.x[i,"d",2*len(model.Nodes)+1] for i in model.Nodes)+sum(model.x[i,"b", 2*len(model.Nodes)+1] for i in model.Nodes)==len(model.Nodes)

def constr_rule3(model):
    return model.y[0]==1

def constr_rule4(model, i, f):
    return sum(model.x[i,l,f] for l in model.Places)==1

def constr_rule5(model, f):
    if f>0:
        return model.y[f]<=model.y[f-1]
    else:
        return Constraint.Skip

def constr_rule6(model, f):
    return sum(model.x[i,"s",f] for i in model.Nodes)+sum(model.x[i,"b",f] for i in model.Nodes)>=model.y[f]

def constr_rule7(model, f):
    return sum(model.x[i,"s",f] for i in model.Nodes)+sum(model.x[i,"b",f] for i in model.Nodes)<=len(model.Nodes)*model.y[f]

def constr_rule8(model, f):
    return sum(model.x[i,"b",f] for i in model.Nodes)<=model.Capacity*model.y[f]

def constr_rule9(model, i, f):
    if f%2==0:
        return model.x[i,"s",f]+model.x[i, "b", f]<=model.x[i,"s",f+1]+model.x[i, "b", f+1]
    else:
        return Constraint.Skip

def constr_rule10(model, i, f):
    if (f%2!=0) & (f<(2*len(model.Nodes))):
        return model.x[i,"d",f]+model.x[i, "b", f]<=model.x[i,"d",f+1]+model.x[i, "b", f+1]
    else:
        return Constraint.Skip

def constr_rule11(model, i, f):
    return model.x[i[0],"s",f]+model.x[i[1], "s", f]<=1

def constr_rule12(model, i, f):
    return model.x[i[0],"d",f]+model.x[i[1], "d", f]<=2-model.y[f]
	
def buildmodel():
    model=ConcreteModel()
    model.Places = Set(initialize=Places)
    model.Trips = Set(initialize=Trips)
    model.Edges = Set(initialize=Edges)
    model.Nodes=Set(initialize=Nodes)
    model.Capacity = Param(mutable=True)
    model.Capacity.value = c
    # variables
    model.x = Var(model.Nodes, model.Places,model.Trips, domain=Boolean)
    model.y=Var(model.Trips, domain=Boolean)
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
    model.constrs9 =  Constraint(model.Nodes, model.Trips,rule=constr_rule9)
    model.constrs10 =  Constraint(model.Nodes, model.Trips,rule=constr_rule10)
    model.constrs11 =  Constraint(model.Nodes, model.Trips,rule=constr_rule11)
    model.constrs12 =  Constraint(model.Nodes, model.Trips,rule=constr_rule12)
    return model

if __name__ == '__main__':
    import sys
    model = buildmodel()
    opt = SolverFactory('cplex_persistent')
    opt.setInstance(model)
    res = opt.solve(tee=True)
    for p in model.x:
	    print("x[{}] = {}".format(p, value(model.x[p])))