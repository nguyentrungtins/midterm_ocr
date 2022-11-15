import cv2
import insert

imagePath = r"./src/image.png"



def toBinaryImg():
  image = cv2.imread(imagePath)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
	
  (thresh, blackAndWhiteImage) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  # result= cv2.bitwise_and(gray, gray, mask=binary)
  return blackAndWhiteImage
  
img = toBinaryImg()

insert.insertID(img,"51900640-51900777")
filename = "./output/ex1_e/"+"image"+".png"
cv2.imwrite(filename,img)

#show image
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()