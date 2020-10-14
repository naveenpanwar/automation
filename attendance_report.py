import csv, sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

csv_file = sys.argv[1]

names = open(csv_file)

attendance_report = {}

csv_reader = csv.reader(names, delimiter=";")
row_num = 0
headers_row = []

for row in csv_reader:
    if row_num == 0:
        row_num+=1
        headers_row = row
        continue
    else:
        row_num+=1
        class_name = row[2]+'-'+row[3]
        if class_name not in attendance_report.keys():
            attendance_report[class_name] = []
        
        for i in range(4, len(row)):
            subject = headers_row[i]
            try:
                attendance = int(row[i][:-1])
                if attendance > 0:
                    if subject not in attendance_report[class_name]:
                        attendance_report[class_name].append(subject)
            except ValueError:
                continue

print("Rows Scanned : "+str(row_num))
pp.pprint(attendance_report)
