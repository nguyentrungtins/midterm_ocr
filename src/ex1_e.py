import cv2
import insert
import numpy as np

imagePath = r"./src/image.png"



def toBinaryImg():
  image = cv2.imread(imagePath)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
  # Nếu chỉ dùng 1 threshold thì sẽ có một ngôi sao không được tô màu nên ta phải dùng nhiều threshold
	# Lấy threshold của ngoi sao bị lỗi
  (thresh, th1) = cv2.threshold(gray, 190, 255, cv2.THRESH_TOZERO_INV)
  

  # đảo chiều threshold lại để tô màu các ngôi sao còn lại
  (thresh, th2) = cv2.threshold(th1, 170, 255, cv2.THRESH_BINARY)
  # cv2.imshow('',th2)
  
  # Đảo threshold lại để khử nhiễu ở các ngôi sao 
  (thresh, th3) = cv2.threshold(th2, 10, 255, cv2.THRESH_BINARY_INV)
  
  #khử nhiễu
  kernel = np.ones((2,2), np.uint8)
  closing = cv2.morphologyEx(th3, cv2.MORPH_CLOSE, kernel)

  #khi nãy đã đổi chiều để khử nhiễu thì giờ ta sẽ đổi chiều lại để  đúng với đề bài
  (thresh, th4) = cv2.threshold(closing, 10, 255, cv2.THRESH_BINARY_INV)
  # cv2.imshow('',th4)
  return th4
  
img = toBinaryImg()

insert.insertID(img,"51900640-51900777")
filename = "./output/ex1_e/"+"image"+".png"
cv2.imwrite(filename,img)

cv2.waitKey(0)

