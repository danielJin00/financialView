import csv
import os, os.path
import glob
import pandas as pd
import matplotlib

#"Auftragskonto";"Buchungstag";"Valutadatum";"Buchungstext";"Verwendungszweck";"Glaeubiger ID";"Mandatsreferenz";"Kundenreferenz (End-to-End)";"Sammlerreferenz";"Lastschrift Ursprungsbetrag";"Auslagenersatz Ruecklastschrift";"Beguenstigter/Zahlungspflichtiger";"Kontonummer/IBAN";"BIC (SWIFT-Code)";"Betrag";"Waehrung";"Info"

anzahl_monate = len((os.listdir("/home/daniel-jin/Documents/Coding/Python_Projects/financialView/Data_Months_csv")))
data = []
header = []
rows = []
csv_path = "/home/daniel-jin/Documents/Coding/Python_Projects/financialView/Data_Months_csv"
filename = "SK_Umsatz_2022_"

for f in range(anzahl_monate):
    with open(f"{csv_path}/{filename}{f+1}.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile) # creating a csv reader object
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)

print(header)
print(rows)






#TODO:
# Print all data in list



