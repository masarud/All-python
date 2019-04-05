# -*- coding: utf-8 -*-
import csv
data = [["トップガン", "Risky Buisiness", "Minority Report"], ["タイタニック", "The Revenant", "Inception"], ["Training Day", "Man On Fire", "Flight"]]
with open("9-4-result.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for i in range(3):
        w.writerow(data[i])
