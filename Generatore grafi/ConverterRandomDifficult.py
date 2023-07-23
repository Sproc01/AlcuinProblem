import os

#files=os.listdir("Grafi")
files=os.listdir("GrafiCasuali")
try:
    files.remove(".DS_Store")
except:
    pass
for i in files:
    for j in range(0, 5):
        file=open("GrafiCasuali/"+i, "r")
        w=open("ConvertitiCasuali/data_"+i[:len(i)-4]+"_"+str(j)+".dat", "w")
        con=file.read()
        file.close()
        w.write("set Places := s b d ;\n")
        w.write("set Nodes := ")
        l=con.split("\n")[3:-1]
        cont=0
        for s in l:
            if len(s)>0:
                s=s.split(" ")
                w.write(s[0]+" ")
                cont+=1
        w.write(";\nset Edges:= ")
        for t in l:
            l1=t.split(" ")
            for k in range(1, len(l1)):
                w.write(str(l1[0])+"-"+str(l1[k])+" ")
        w.write(";\n")
        w.write("set Trips := ")
        for k in range(0,2*cont+2):
            w.write(str(k)+" ")
        w.write(";\n\n")
        p=con.index("!")
        capacity=int(con[p+1:])-j
        w.write("param Capacity :="+str(capacity)+";\n")
        w.write("param len := "+str(cont)+";\n")
        w.close()