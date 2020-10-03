import csv
import sys

from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_file = sys.argv[1]
csv_file = sys.argv[2]

names = open(csv_file)
students = []

csv_reader = csv.reader(names, delimiter=";")
for row in csv_reader:
    students.append(row)

inputpdf = PdfFileReader(open(pdf_file, "rb"))
total = 1
skipped = 1

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    page = inputpdf.getPage(i)
    text = page.extractText()
    CONST = "Name of the student\n:"
    start = text.find(CONST) + len(CONST)+2
    end = text.find("\n", start)
    student_name = text[start:end]
    school_num = ""
    for row in students:
        if student_name in row:
            print(total, row[0], row[1])
            school_num = row[0]
            total+=1
            break
    output.addPage(page)
    if school_num == "":
        with open("skipped_"+str(skipped)+".pdf","wb") as outputStream:
            output.write(outputStream)
            skipped+=1
    else:
        with open(school_num+".pdf", "wb") as outputStream:
            output.write(outputStream)

print("Total: Renamed:"+str(total-1)+" Not Renamed:"+str(skipped-1))
