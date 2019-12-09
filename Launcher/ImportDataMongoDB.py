import pymongo
import csv
import json

## installer pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')

db = client.catalogue

catalogue = db.catalogue

filename = 'CatalogueTraitee.csv'
jsonCatalogue = 'jsonCatalogue.json'

catalogueData = {}

## Cleaning CatalogueTraitee.csv to be sure that it's empty ##
print("Cleaning jsonCatalogue.json...")
with open("../Donnees/" + jsonCatalogue,"w") as file:
    file.write('')
    file.close()

## Creating Catalogue JSON ready to be imported to MongoDB ##
with open("../Donnees/CatalogueTraitee.csv","r") as csvFile:
    csvReader = csv.DictReader(csvFile)
    i = 0
    for line in csvReader:
        catalogueData[str(i)] = line
        print(line)
        i = i + 1
    print(" ")
    print("## Copying " + str(i) + " lines from " + filename + " ##")

csvFile.close()

## Writing new JSON file with elements ##
with open("../Donnees/" + jsonCatalogue, 'a') as jsonFile:
    jsonFile.write(json.dumps(catalogueData, indent=4))
jsonFile.close()

## Reading JSON file to import into MongoDB ##
with open("../Donnees/" + jsonCatalogue, 'r') as jsonFile:
    file_data = json.load(jsonFile)
    one_data = json.dumps(file_data, indent=1)
    ##getElement = file_data.get("1")
    ##print("Value : " + str(getElement))
    i = 0
    for element in range(0, len(file_data)):
        mongoResponse = catalogue.insert_one(file_data.get(str(i)))
        i = i + 1
jsonFile.close()
