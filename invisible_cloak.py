import cv2
from cv2 import morphologyEx
from cv2 import MORPH_DILATE
import numpy as np

cap = cv2.VideoCapture(0)
background= cv2.imread('./image.jpg')

while cap.isOpened():
    ret, current_frame= cap.read()

    if ret:

        new_image=cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        lower_red= np.array([0,120,70])
        upper_red= np.array([10,255,255])
        masking_1= cv2.inRange(new_image, lower_red, upper_red)

        lower_red= np.array([170,120,70])
        upper_red= np.array([180,255,255])
        masking_2= cv2.inRange(new_image, lower_red, upper_red)

        red_mask= masking_1 + masking_2

        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=10)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1)

        part1 = cv2.bitwise_and(background, background, mask= red_mask)

        not_red=cv2.bitwise_not(red_mask)
        
        part2 = cv2.bitwise_and(current_frame, current_frame, mask=not_red)



        cv2.imshow("invisible cloak", part1+part2)
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()










