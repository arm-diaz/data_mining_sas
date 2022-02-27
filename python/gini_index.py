import numpy as np
import pandas as pd


def gini(list_of_values):
    sorted_list = sorted(list(list_of_values))
    height, area = 0, 0
    for value in sorted_list:
        height += value
        area += height - value / 2.
    fair_area = height * len(list_of_values) / 2
    return (fair_area - area) / fair_area


df = pd.read_excel("../data/midterm data.xlsx")

print(df["Holiday"])
print(gini(df["Holiday"].values))
