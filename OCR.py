import pytesseract
from PIL import ImageGrab
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = ImageGrab.grabclipboard()
ocr_result = pytesseract.image_to_string(img)
print(ocr_result)
input("Press enter to conitnue....")
