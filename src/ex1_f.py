import cv2
import numpy as np
import insert 
# Let's load a simple image with 3 black squares
image = cv2.imread("src/image.png")
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(edged,
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)

insert.insertID(image,"51900640-51900777")
filename = "./output/ex1_f/"+"image"+".png"
cv2.imwrite(filename,image)

