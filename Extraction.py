import os

files=os.listdir('Res/')
for i in files:
    file=open('Res/'+i,'r')
    lines=file.readlines()
    file.close()
    file=open('Risultati.csv','a')
    file.write(lines[0]+'\n')
    file.close()