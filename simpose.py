from PIL import Image, ImageFont, ImageDraw
import os
import csv

def make_name(img_name, name):
    img = Image.open("students/"+img_name)
    img = img.resize((405, 575), Image.ANTIALIAS)
    width, height = img.size

    layer = Image.new("RGB", (width, height + 20), (255,255,255))
    font = ImageFont.truetype("arial.ttf",18)
    layer.paste(img)

    output = ImageDraw.Draw(layer)
    w, h = output.textsize(name, font)
    output.multiline_text(((width-w)/2,height), name, fill=(0, 0, 0), font=font, align="right")
    layer.save("students_output/"+img_name)

names = open("9_11.csv")
students = []
count = 0

csv_reader = csv.reader(names, delimiter=";")
for row in csv_reader:
    students.append(row)

files = os.listdir("students")

for s in students:
    if s[0]+".JPG" in files:
        count+=1
        make_name(s[0]+".JPG", s[1])
    elif s[0]+".jpg" in files:
        count+=1
        make_name(s[0]+".jpg", s[1])
    else:
        print(s)

print("Total Files = "+str(len(files)))
print("Total = "+str(count))
print("Total Students = "+str(len(students)))
