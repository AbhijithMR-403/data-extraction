import pytesseract
from PIL import Image


# pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract'
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR'



val = pytesseract.image_to_string(Image.open('del_files/0Im0.jpg'))
val = pytesseract.image_to_string('del_files/0Im0.jpg')
