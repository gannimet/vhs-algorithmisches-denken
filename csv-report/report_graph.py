import csv
import matplotlib.pyplot as plt

# 1. CSV einlesen
with open("./csv-report/quarters.csv", encoding="utf-8") as f:
    zeilen = list(csv.DictReader(f))

# 2. Daten umsortieren: Quartale, Regionen und ein Nachschlage-Dict aufbauen
quartale = []   # x-Achse, in Reihenfolge der Datei
regionen = []   # eine Balkengruppe pro Region
werte = {}      # (Region, Quartal) -> Umsatz

for zeile in zeilen:
    label = f'{zeile["Quartal"]} {zeile["Jahr"]}'
    region = zeile["Region"]
    
    if label not in quartale:
        quartale.append(label)
        
    if region not in regionen:
        regionen.append(region)
        
    werte[(region, label)] = int(zeile["Umsatz_EUR"])

# 3. Balkendiagramm zeichnen
farben = ["steelblue", "darkorange", "seagreen"]
balkenbreite = 0.25

for i in range(len(regionen)):
    region = regionen[i]
    hoehen = [werte[(region, label)] for label in quartale]
    positionen = [pos + i * balkenbreite for pos in range(len(quartale))]
    plt.bar(positionen, hoehen, width=balkenbreite, color=farben[i], label=region)

mitte = [pos + balkenbreite for pos in range(len(quartale))]

plt.xticks(mitte, quartale, rotation=45, ha="right")
plt.ylabel("Umsatz (EUR)")
plt.title("Quartalsumsätze nach Region")
plt.legend()
plt.tight_layout()
plt.show()