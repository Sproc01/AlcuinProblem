import os

files=os.listdir("Grafi")
files.remove(".DS_Store")
for i in files:
    file=open("Grafi/"+i, "r")
    w=open("Convertiti/data_"+i[:len(i)-4]+".dat", "w")
    con=file.read()
    file.close()
    w.write("set Places := s b d ;\n")
    w.write("set Nodes := ")
    l=con.split("\n")[3:-1]
    cont=0
    for i in l:
        if len(i)>0:
            i=i.split(" ")
            w.write(i[0]+" ")
            cont+=1
    w.write(";\nset Edges:= ")
    for i in l:
        l1=i.split(" ")
        for i in range(1, len(l1)):
            w.write(str(l1[0])+"-"+str(l1[i])+" ")
    w.write(";\n")
    w.write("set Trips := ")
    for i in range(0,2*cont+2):
        w.write(str(i)+" ")
    w.write(";\n\n")
    p=con.index("!")
    w.write("param Capacity :="+con[p+1:]+";\n")
    w.write("param len := "+str(cont)+";\n")
    w.close()
    
        