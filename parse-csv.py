import csv

reader = csv.reader(open("authors.csv"))
for row in reader:
     for i,field in enumerate(row):
          if i < len(row)-1:
               print(field.strip(), end=", ")
          else:
               print(field.strip(), end="\n")
