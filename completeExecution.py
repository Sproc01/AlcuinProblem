import os

files=os.listdir("Generatore grafi/ConvertitiCasuali")
files.sort()
try:
    files.remove(".DS_Store")
except:
    pass
for i in files:
    print('Execution of python3 Model.py Generatore\ grafi/ConvertitiCasuali/'+i+' with seed=0')
    command=os.popen('python3 Model.py Generatore\ grafi/ConvertitiCasuali/'+i+' 0')
    res=command.read()
    file=open('Output terminale/Res_'+i[:len(i)-4]+'.txt','w')
    file.write(res)
    file.close()