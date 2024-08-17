import cv2
import random

img = cv2.imread('assets/1.jpg', -1)

print(img[257][400])

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


























# [
# # regulary its gonna be rd green blue but in open CV its gonn be blue green red.
# [[0, 0, 0], [255, 255, 255]], 
# [[0, 0, 0], [255, 255, 255]],
# ]

