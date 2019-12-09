import cx_Oracle
import csv

dsn = cx_Oracle.makedsn(
    '134.59.152.116', 
    '443', 
    service_name='pdbmbds.unice.fr'
)
con = cx_Oracle.connect(
    user='ors1', 
    password='Pass1', 
    dsn=dsn
)
cur = con.cursor()
with open("../Donnees/Clients_12Traitee.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    cur.execute("drop table Clients_12")
    cur.execute("create table Clients_12(age varchar2(255), sexe varchar2(255), taux varchar2(255), situationFamiliale varchar2(255), nbEnfantsAcharge varchar2(255), deuxiemeVoiture varchar2(15), immatriculation varchar2(255))")
    for lines in csv_reader:
        cur.execute(
            "insert into Clients_12 (age,sexe,taux,situationFamiliale,nbEnfantsAcharge,deuxiemeVoiture,immatriculation) values (:1, :2, :3, :4, :5, :6, :7)",
            (lines['age'], lines['sexe'], lines['taux'], lines['situationFamiliale'], lines['nbEnfantsAcharge'], lines['deuxiemeVoiture'], lines['immatriculation']))
cur.close()
con.commit()
con.close()
