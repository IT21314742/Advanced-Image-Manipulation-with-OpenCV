import cv2

img = cv2.imread('assets/1.jpg', -1)

print(img)

# [
# # regulary its gonna be rd green blue but in open CV its gonn be blue green red.
# [[0, 0, 0], [255, 255, 255]], 
# [[0, 0, 0], [255, 255, 255]],
# ]

