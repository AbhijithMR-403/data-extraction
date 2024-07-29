from pypdf import PdfReader 
import cv2
import pytesseract

# creating a pdf reader object 
reader = PdfReader('example-files/Wipro.pdf') 
  
# printing number of pages in pdf file 
print(len(reader.pages)) 

pp = reader.pages[0]
# print(dir(pp))
for count, image_file_object in enumerate(pp.images):
    with open("del_files/"+str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)

image = cv2.imread('del_files/0Im0.jpg')
text = pytesseract.image_to_string(image)
print(text)

# print(pp.extract_text())