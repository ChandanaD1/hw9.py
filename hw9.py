import csv
import pandas as pd
import plotly.express as px
import math

with open("hw9.csv") as file1:
    reader = csv.reader(file1)
    data = list(reader)

marks = []

for x in data:
    value = float(x[0])
    marks.append(value)

total = 0
for x in marks:
    total = total + x

n = len(marks)

mean = total/n
print(mean)

sum = 0
for x in marks:
    difference = x - mean
    square = difference * difference
    sum = sum + square

deviant = math.sqrt(sum/(n-1))
print(deviant)