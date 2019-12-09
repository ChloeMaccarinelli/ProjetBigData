import string
import csv
import sys
import unicodedata
from unidecode import unidecode
reload(sys) 
sys.setdefaultencoding("latin-1")

fileNames = ["Catalogue", "Clients_4", "Clients_12", "Immatriculations", "Marketing"]

######## FILTERING FILES ########

for currentFilename in fileNames:
    filename = currentFilename + '.csv'
    ## Calculating lines to convert
    initialFile= open(filename,"r")
    i = 0
    for line in initialFile.readlines():
        i = i + 1
    initialFile.close()
    
    print(" ")
    print("## Copying " + str(i) + " lines from " + filename + " ##")

    ## Starting conversion process
    #initialFile= open(filename,"rw+")
    initialFile= open(filename,"r")
    filenameTraitee = currentFilename + "Traitee.csv"
    print("Cleaning " + filenameTraitee)
    with open(filenameTraitee,'w') as f :
        f.write('')
        f.close()

    print("Converting " + filename + " into " + filenameTraitee)
    print("Please wait until the conversion is over")
    j = 0
    with open(filenameTraitee, 'a') as file:
        for line in initialFile.readlines():
            ## replace same words
            line.replace('Masculin','M').replace('Homme','M').replace('Feminin','F')
            file.write(unidecode(line))            
            j = j + 1

    ## Quick veryfiying that all lines are parsed
    print("Verifying if there's no line loss")

    if i == j:
        print("All lines are properly parsed")
    else:
        print("There's probably some line loss, please verify your files")
        print("i = " + str(i))
        print("j = " + str(j))

    file.close()
    initialFile.close()
