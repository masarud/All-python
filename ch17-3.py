import re

text = "The ghost that says boo haunts the loo"
pattern = ".oo"

found = re.findall(pattern, text)
print(found)