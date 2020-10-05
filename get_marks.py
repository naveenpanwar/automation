import csv
import sys

from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_file = sys.argv[1]

inputpdf = PdfFileReader(open(pdf_file, "rb"))
total = 1
skipped = 1

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    page = inputpdf.getPage(i)
    text = page.extractText()
    CONST = "School No.:"
    start = text.find(CONST) + len(CONST)+9
    end = text.find("\n", start)
    school_number = text[start:end]
    print(school_number)
    output.addPage(page)
    if text.find(CONST) == -1:
        with open(str(skipped)+"_marks.pdf", "wb") as outputStream:
            output.write(outputStream)
            skipped+=1
    else:
        with open(school_number+"_marks.pdf", "wb") as outputStream:
            output.write(outputStream)
            total+=1

print("Total: Renamed:"+str(total-1)+" Not Renamed:"+str(skipped-1))
