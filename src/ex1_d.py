import cv2
import insert
imagePath = r"./src/image.png"



def toBinaryImg():
  image = cv2.imread(imagePath)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  # Set threshold and maximum value
  thresh = 220
  maxValue = 255

  # Binary Threshold
  th, binary = cv2.threshold(gray, thresh, maxValue, cv2.THRESH_BINARY_INV)

  result= cv2.bitwise_and(gray, gray, mask=binary)
  return result
  
img = toBinaryImg()

insert.insertID(img,"51900640-51900777")
filename = "./output/ex1_d/"+"image"+".png"
cv2.imwrite(filename,img)

