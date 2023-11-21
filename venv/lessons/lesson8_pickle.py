import csv
import pickle
import os

## pickle
# below read a csv file, convert to list, then convert to byte string finally write in a file
with open("./csv_files/workers.csv", "r", encoding="utf-8") as csv_f:
    raw_data = list(csv.reader(csv_f))

header_lst = raw_data[0]
body_lst = raw_data[1:]
final_lst = list()
final_lst.append(header_lst)
final_lst.append(body_lst)
with open("./picke_files/workers.pickle", "wb") as pf:
    pickle.dump(final_lst, pf)

# below I am trying to read bytes from file that was created higher
with open("./picke_files/workers.pickle", "rb") as pf:
    raw_data = pickle.load(pf)

for header in raw_data[0]:
    print(f"{header:>10}", end="\t")
print()
for body in raw_data[1:]:
    for line in body:
        for i in line:
            print(f"{i:>10}", end="\t")
        print()
print()