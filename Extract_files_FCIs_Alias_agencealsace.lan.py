import os, subprocess
import zipfile
import shutil
import re
import csv

FCIzipFolder = '\\\\fs-ld.agencealsace.lan\\Losange-Deploiement\\Direction Ingenierie\\Public\\TRAVAIL_PERSONNEL\\THIBAUT_RONDEAU\\GCBLO Fichiers Semaines\\'
outputFolder = '\\\\fs-ld.agencealsace.lan\\Losange-Deploiement\\Direction Ingenierie\\Public\\INFRATIERS\\ORANGE\\Outils\\Outil Récupération Fichiers GCBLO\\RESULTAT\\'
inputFolder = '\\\\fs-ld.agencealsace.lan\\Losange-Deploiement\\Direction Ingenierie\\Public\\INFRATIERS\\ORANGE\\Outils\\Outil Récupération Fichiers GCBLO\\ENTREE\\'
inputFile = 'Liste_FCIs.txt'

if os.path.exists(outputFolder):
    shutil.rmtree(outputFolder)
os.mkdir(outputFolder)

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                 
def get_files (entry_path):

    listes_fci = list()
    cpt = 0
    
    filename = os.path.normpath(inputFolder+'/'+inputFile)
    
    with open(filename, "r") as f_in:
        lines = f_in.readlines()
        
        for line in lines:
            if (line[0]=='F' and (len(line)== 12 or len(line)== 13)) and (cpt == 0 or (line not in listes_fci)):
                listes_fci.insert(cpt, line[0:12])
                cpt += 1

    print(listes_fci)
    total_count = 0
    for root, dirs, files in os.walk(FCIzipFolder):
        for file in files:
            current_fci = file[16:28]
            if current_fci in listes_fci and not os.path.exists(os.path.normpath(outputFolder+'/'+file)):
                gcbfile = os.path.normpath(root+'/'+file)
                shutil.copyfile(gcbfile, os.path.normpath(outputFolder+'/'+file))
                total_count += 1
                
    return total_count
    
compteur = get_files (inputFolder)
print(compteur)
