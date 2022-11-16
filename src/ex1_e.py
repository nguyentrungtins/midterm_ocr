import cv2
import insert
import numpy as np

imagePath = r"./src/image.png"



def toBinaryImg():
  image = cv2.imread(imagePath)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
	
  (thresh, th1) = cv2.threshold(gray, 190, 255, cv2.THRESH_TOZERO_INV)
  

  (thresh, th2) = cv2.threshold(th1, 170, 255, cv2.THRESH_BINARY)
  

  (thresh, th3) = cv2.threshold(th2, 10, 255, cv2.THRESH_BINARY_INV)
  

  kernel = np.ones((2,2), np.uint8)
  closing = cv2.morphologyEx(th3, cv2.MORPH_CLOSE, kernel)

  (thresh, th4) = cv2.threshold(closing, 10, 255, cv2.THRESH_BINARY_INV)
  return th4
  
img = toBinaryImg()

insert.insertID(img,"51900640-51900777")
filename = "./output/ex1_e/"+"image"+".png"
cv2.imwrite(filename,img)

cv2.waitKey(0)

