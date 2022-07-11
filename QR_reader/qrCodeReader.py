
###############libraries
# OpenCv library
import cv2
# pyzbar library
import pyzbar.pyzbar as pyzbar
from datetime import datetime

# Camera Resolution
width = 640
height = 480
# Capturing Video
camera = cv2.VideoCapture(0)
# Camera Settings
camera.set(3,width)
camera.set(4,height)

# The QR decoder function with an image input
def decodeCam(image):
    # Converting the image to a gray-scale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Decoding the code using pyzbar (it can detect multiple qrcode simultaneously and the type (barcode/QRcode))
    barcodes = pyzbar.decode(gray)
    print('reading...', end='\r')
    # Extracting data and type of each barcode
    for barcode in barcodes:
        barcodeData = barcode.data.decode()
        barcodeType = barcode.type
        print("["+str(datetime.now())+"] Type:{} | Data: {}".format(barcodeType, barcodeData))
    return image

# The main loop
try:
 while True:
  # Read current frame
  ret, frame = camera.read()
  im=decodeCam(frame)
except KeyboardInterrupt:
 print('interrupted!')
