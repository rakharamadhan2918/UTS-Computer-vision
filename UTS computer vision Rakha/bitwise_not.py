import cv2
import numpy as np
import os

 
os.makedirs("output", exist_ok=True)
canvas = np.full((400, 400, 3), 255, dtype=np.uint8)

cv2.rectangle(canvas, (140, 180), (260, 320), (150, 100, 50), -1)  
pts = np.array([[200, 100], [130, 180], [270, 180]], np.int32)
cv2.fillPoly(canvas, [pts], (100, 60, 30))  
cv2.circle(canvas, (200, 230), 25, (0, 0, 0), -1)
cv2.rectangle(canvas, (190, 320), (210, 370), (80, 50, 20), -1)
cv2.line(canvas, (180, 260), (220, 260), (0, 0, 0), 4)

cv2.imwrite("output/rumah_burung.png", canvas)

background = np.full((400, 400, 3), (180, 255, 180), dtype=np.uint8)
bitwise_not = cv2.bitwise_not(canvas)
cv2.imwrite("output/bitwise_not.png", bitwise_not)
