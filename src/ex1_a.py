import cv2
import insert
import numpy as np
color_list = [
    ['red' ,[0, 100, 20], [0, 255, 255], [159, 50, 70], [180, 255, 255]],
    ['green' ,[0, 100, 20], [0, 255, 255], [36, 50, 70], [89, 255, 255]],
    ['blue' ,[0, 100, 20], [0, 255, 255], [90, 50, 70], [128, 255, 255]],
    ['yellow' ,[0, 100, 20], [0, 255, 255], [25,100,20], [35, 255, 255]],
    ['purple' ,[0, 100, 20], [0, 255, 255], [129, 50, 70], [158, 255, 255]], 
    ['orange' ,[0, 100, 20], [0, 255, 255], [1, 190, 200], [18, 255, 255]],
]



for color_name, lower1, upper1, lower2, upper2 in color_list:
    img = cv2.imread("src/image.png")
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_mask = cv2.inRange(hsv_img, np.array(lower1), np.array(upper1))
    upper_mask = cv2.inRange(hsv_img, np.array(lower2), np.array(upper2))

    full_mask = lower_mask + upper_mask
  
    result= cv2.bitwise_and(img, img, mask=full_mask)
    insert.insertID(result,"51900640-51900777")
    filename = "./output/ex1_a/"+color_name+".png"
    cv2.imwrite(filename,result)



