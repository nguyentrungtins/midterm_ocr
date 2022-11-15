import cv2
def insertID(image,ID):
    
    # image = cv2.imread(path)
    
    
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # org
    org = (50,50)
    
    # fontScale
    fontScale = 1
    
    # Blue color in BGR
    color = (255, 0 ,0)
    
    # Line thickness of 2 px
    thickness = 1
    
    # Using cv2.putText() method
    image = cv2.putText(image, ID, org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    return image

