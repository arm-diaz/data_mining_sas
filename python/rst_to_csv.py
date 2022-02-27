from striprtf.striprtf import rtf_to_text
import re
import pandas as pd

with open("../data/midterm_fitness_data.rtf") as infile:
    content = infile.read()
    text = rtf_to_text(content)

ls = text.split(";")
header = ls[1].strip().split(" ")[1:-1]
tmp_data = [re.sub(' +', ' ', v.strip()) for v in ls[3].strip().split("\n")]
data = []
for v in tmp_data:
    data.append(v.split(" ")[0:4])
    data.append(v.split(" ")[4:])
data.remove([])

df = pd.DataFrame(data, columns=header)
for c in df.columns:
    df[c] = pd.to_numeric(df[c], errors='coerce')
df.to_csv("../data/midterm_fitness_data.csv", index=False)