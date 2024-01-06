import pytesseract
from PIL import ImageGrab
import cv2
from tkinter import *
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def printing(img):
    ocr_result = pytesseract.image_to_string(img)
    print(ocr_result)

def clipboardcmd():
    img = ImageGrab.grabclipboard()
    printing(img)

def capturecmd():
    cap = cv2.VideoCapture(0)  # 0 for default camera
    result, img = cap.read()
    if result: 
        # showing result, it take frame name and image  
        # output 
        cv2.imshow("Clicked", img) 
        # If keyboard interrupt occurs, destroy image  
        # window 
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
        del cap
    printing(img)

root = Tk()
root.geometry("100x100")
clip = Button(root, text = "Clipboard", command = clipboardcmd)
clip.pack()
photo = Button(root, text = "Photo", command = capturecmd)
photo.pack()

root.mainloop()