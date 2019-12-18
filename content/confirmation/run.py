import numpy as np
import subprocess
import os

mem_list = []
members = open("participants.txt", 'r')
for line in members:
    mem_list.append(line.replace("\n", ""))

for name in mem_list:
    file_name = "confirmation_" + name.replace(" ", "_").replace(".", "_").replace("ö", "oe").replace("ü", "ue").replace("ä", "ae").replace("ß", "sss")  + ".tex"
    with open("confirmation_template.tex") as f:
        templateText=f.read().replace('PLATZHALTER-NAMEN', name)
    with open(file_name, "w") as f:
        f.write(templateText)
    commandLine = subprocess.Popen(['pdflatex', file_name], cwd=os.getcwd())
    commandLine.communicate()
    subprocess.call('rm *log *svg *aux *gz {}'.format(file_name), cwd=os.getcwd(), shell=True)
