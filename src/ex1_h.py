import cv2
import numpy as np
import insert 
# Let's load a simple image with 3 black squares
image = cv2.imread("src/image.png")

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)


insert.insertID(image_sharp,"51900640-51900777")
filename = "./output/ex1_h/"+"image"+".png"
cv2.imwrite(filename,image_sharp)


