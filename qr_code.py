import cv2
!apt install libzbar0
!pip install pyzbar
import numpy as np
from pyzbar.pyzbar import decode
from google.colab.patches import cv2_imshow
def get_coordinates(image_name):
  img=cv2.imread(image_name)
  decoded=decode(img)
  for obj in decoded:
    print("Data: ",obj.data)
  ret_qr, points = cv2.QRCodeDetector().detect(img)
  print(points)
get_coordinates('qr.jpeg')