from tokenize import Double
from pyomo.environ import *
from pyomo.opt import SolverFactory

#lettura stringa res
def get_info_from_results(results, info_string):
    i = str(results).lower().find(info_string.lower()) + len(info_string)
    value = ''
    while str(results)[i] != '\n':
        value = value + str(results)[i]
        i += 1
    return value


def obj_rule(model):#f.obiettivo
    return sum(model.y[f] for f in model.Trips)-1

def constr_rule1(model):#vincolo di partenza
    return sum(model.x[i,"s",0] for i in model.Nodes)==model.len

def constr_rule2(model):#vincolo di arrivo
    return sum(model.x[i,"d",2*model.len+1] for i in model.Nodes)+sum(model.x[i,"b", 2*model.len+1] for i in model.Nodes)==model.len

def constr_rule3(model):#vincolo di partenza y
    return model.y[0]==1

def constr_rule4(model, i, f):#vincolo un oggetto in un solo luogo
    return sum(model.x[i,l,f] for l in model.Places)==1

def constr_rule5(model, f):#vincolo di progressione y
    if f>0:
        return model.y[f]<=model.y[f-1]
    else:
        return Constraint.Skip

def constr_rule6(model,f): #vincolo legame y x 1
    return sum(model.x[i,"s",f] for i in model.Nodes)+sum(model.x[i,"b",f] for i in model.Nodes)>=model.y[f]

def constr_rule7(model, f): #vincolo legame y x 2
    return sum(model.x[i,"s",f] for i in model.Nodes)+sum(model.x[i,"b",f] for i in model.Nodes)<=model.len*model.y[f]

def constr_rule8(model, f): #vincolo capacità
    return sum(model.x[i,"b",f] for i in model.Nodes)<=model.Capacity*model.y[f]

def constr_rule9(model, i, f): #vincolo gite pari
    if f%2==0:
        return model.x[i,"s",f]+model.x[i, "b", f]==model.x[i,"s",f+1]+model.x[i, "b", f+1]
    else:
        return Constraint.Skip

def constr_rule10(model, i, f): #vincolo gite dispari
    if (f%2!=0) and (f<(2*model.len+1)):
        return model.x[i,"d",f]+model.x[i, "b", f]==model.x[i,"d",f+1]+model.x[i, "b", f+1]
    else:
        return Constraint.Skip

def constr_rule11(model, i, f): #stable set a sinistra
    #aggiunta
    l=i.split("-")
    #------
    if f>0:
        return model.x[int(l[0]),"s",f]+model.x[int(l[1]), "s", f]<=1
    else:
        return Constraint.Skip

def constr_rule12(model, i, f): #stable set a destra
    #aggiunta
    l=i.split("-")
    #------
    return model.x[int(l[0]),"d",f]+model.x[int(l[1]), "d", f]<=2-model.y[f]
	
def buildmodel():
    model=AbstractModel()
    model.Places = Set()
    model.Trips = Set()
    model.Edges = Set()
    model.Nodes=Set()
    model.Capacity = Param()
    model.len=Param()
    # variables
    model.x = Var(model.Nodes, model.Places,model.Trips, domain=Boolean)
    model.y=Var(model.Trips, domain=Boolean)
    # objective
    model.obj = Objective(rule=obj_rule, sense=minimize)
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
    model.constrs11 =  Constraint(model.Edges, model.Trips,rule=constr_rule11)
    model.constrs12 =  Constraint(model.Edges, model.Trips,rule=constr_rule12)
    return model

if __name__ == '__main__':
    import sys
    model = buildmodel()
    opt = SolverFactory('cplex_persistent')
    opt.options['randomseed']=100
    s=sys.argv[1]
    instance = model.create_instance(s)
    opt.set_instance(instance)
    try:
        v=s[::-1].index("/")
    except:
        v=0
    #opt.write("Modelli_generati/AlcuinAbstract_"+str(s[len(s)-v:len(s)-4])+".lp")
    res = opt.solve(tee=True)
    file=open("Risultati/file_"+str(s[len(s)-v:len(s)-4])+".csv","w")
    upper=get_info_from_results(res,"upper bound: ")
    lower=get_info_from_results(res,"lower bound: ")
    if lower=='None' and upper=='None':
        gap=0
    else:
        gap=float(upper)-float(lower)
    file.write(str(s[len(s)-v:len(s)-4])+";"+get_info_from_results(res, 'Time: ')+";"+lower+";"+upper+";"+str(gap)+';'+get_info_from_results(res, "termination condition: ")+';'+str(instance.Capacity.value)+';'+str(instance.len.value)+"\n")
    file.close()
    #for p in instance.x:
	    #print("x[{}] = {}".format(p, value(instance.x[p])))
    if get_info_from_results(res, "termination condition: ")=='optimal':
        for p in instance.y:
            if value(instance.y[p])==0:
                break
            print("y[{}] = {}".format(p, value(instance.y[p])))