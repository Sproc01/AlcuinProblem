import os

files=os.listdir("Grafi")
files.remove(".DS_Store")
for i in files:
    file=open("Grafi/"+i, "r")
    w=open("Convertiti/vertex_"+i, "w")
    w1=open("Convertiti/edge_"+i, "w")
    con=file.read()
    file.close()
    l=con.split("\n")
    for i in l:
        l1=i.split(" ")
        w.write(l1[0]+" ")
        for i in range(1, len(l1)):
            w1.write(str(l1[0])+str(l1[i])+" ")
    w.close()
    w1.close()
    
