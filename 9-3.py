import csv
data = [["Top Gun", "Risky Buisiness", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man On Fire", "Flight"]]
with open("9-3-result.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for i in range(3):
        w.writerow(data[i])
