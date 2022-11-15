import cv2
import insert
import numpy as np
color_list = [
    ['red', [159, 50, 70], [180, 255, 255]],
    ['green', [36, 50, 70], [89, 255, 255]],
    ['blue', [90, 50, 70], [128, 255, 255]],
    ['yellow', [25, 50, 70], [35, 255, 255]],
    ['purple', [129, 50, 70], [158, 255, 255]], 
    ['orange', [1, 190, 200], [18, 255, 255]],
]

img = cv2.imread("src/image.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

for color_name, lower_val, upper_val in color_list:
    # threshold the HSV image - any matching color will show up as white
    mask = cv2.inRange(hsv_img, np.array(lower_val), np.array(upper_val))
    result= cv2.bitwise_and(img, img, mask=mask)
    insert.insertID(result,"51900640")
    filename = "./output/ex1/"+color_name+".png"
    cv2.imwrite(filename,result)



