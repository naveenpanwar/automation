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
renamed = 1
skipped = 1
left = 1

for i in range(0, inputpdf.numPages, 2):
    output = PdfFileWriter()
    page = inputpdf.getPage(i)
    next_page = inputpdf.getPage(i+1)
    text = page.extractText()
    CONST = "Name of the student\n:"
    output.addPage(page)
    output.addPage(next_page)

    if text.find(CONST) == -1:
        print(text)
        with open("new_data/left_"+str(left)+".pdf","wb") as outputStream:
            output.write(outputStream)
            print("CONTINUE")
        left+=1
    else:
        start = text.find(CONST) + len(CONST)+3
        end = text.find("\n", start)
        student_name = text[start:end]
        school_num = ""
        if student_name == "":
            with open("new_data/left_"+str(left)+".pdf","wb") as outputStream:
                output.write(outputStream)
                print("CONTINUE NAME NOT FOUND")
            left+=1
        else:
            for row in students:
                if student_name in row:
                    school_num = row[0]
            print(total, school_num, student_name)
            if school_num == "":
                with open("new_data/skipped_"+str(skipped)+".pdf","wb") as outputStream:
                    output.write(outputStream)
                    skipped+=1
            else:
                with open("new_data/"+school_num+".pdf", "wb") as outputStream:
                    output.write(outputStream)
                    renamed+=1
    total+=1

print("Total: "+str(total-1)+" Renamed:"+str(renamed)+" Not Renamed:"+str(skipped-1)+" Left: "+str(left))
