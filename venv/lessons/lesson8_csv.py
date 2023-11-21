## CSV
#csv.reader()
import csv

raw_data = list()
with open("./csv_files/workers.csv", "r", newline="") as csv_f:
    raw_data = list(csv.reader(csv_f))

csv_header = list(raw_data[0])
csv_body = list(raw_data[1:])

for line in range(len(csv_body)):
    for ind in range(len(csv_body[line])):
        csv_body[line][ind] = csv_body[line][ind].lower()

#csv.writer(data)
with open("./csv_files/workers.csv", "w", encoding="utf-8") as csv_file:
    csv_w = csv.writer(csv_file)
    csv_w.writerow(csv_header)
    csv_w.writerows(csv_body)

#csv.writerow(line)
#csv.writerows(all_data)