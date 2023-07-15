import os
#!/bin/bash
#SBATCH --job-name=ModelloAlcuin
#SBATCH --partition=arrow
#SBATCH --ntasks=1
#SBATCH --mem=14GB
#SBATCH --mail-user michele.sprocatti@studenti.unipd.it
#SBATCH --output output_%j.txt
#SBATCH --error errors_%j.txt
#SBATCH --mail-type ALL

# warm up processors
#sudo cpupower frequency-set -g performance
#sleep 0.1
#stress-ng -c 4 --cpu-ops=100
# set limits
#ulimit -v 16777216
#####################
# commands to execute
#. ~/.bashrc
#cd /home/sprocatti1/AlcuinProblem
#python3 Model.py Generatore\ grafi/ConvertitiCasuali/data_Graph50_200_1.dat
#####################
# back to power saving mode
#sudo cpupower frequency-set -g powersave
files=os.listdir("Generatore grafi/ConvertitiCasuali")
files.sort()
try:
    files.remove(".DS_Store")
except:
    pass
for i in files:
    print("Sbatch of "+i)
    file=open("Sbatch/Sbatch_"+i[:len(i)-4]+".txt","w")
    file.write('#!/bin/bash\n')
    file.write('#SBATCH --job-name=ModelliAlcuin'+i[:len(i)-4]+'\n')
    file.write('#SBATCH --partition=arrow\n')
    file.write('#SBATCH --ntasks=1\n')
    file.write('#SBATCH --mem=14GB\n')
    file.write('#SBATCH --mail-user michele.sprocatti@studenti.unipd.it\n')
    file.write('#SBATCH --output output_%j.txt\n')
    file.write('#SBATCH --error errors_%j.txt\n')
    file.write('#SBATCH --mail-type ALL\n')
    file.write('# warm up processors\n')
    file.write('sudo cpupower frequency-set -g performance\n')
    file.write('sleep 0.1\n')
    file.write('stress-ng -c 4 --cpu-ops=100\n')
    file.write('# set limits\n')
    file.write('ulimit -v 16777216\n')
    file.write('#####################\n')
    file.write('# commands to execute\n')
    file.write('. ~/.bashrc\n')
    file.write('cd /home/sprocatti1/AlcuinProblem\n')
    file.write('python3 Model.py Generatore\ grafi/ConvertitiCasuali/'+i+'\n')
    file.write('#####################\n')
    file.write('# back to power saving mode\n')
    file.write('sudo cpupower frequency-set -g powersave')
    file.close()