import cv2
import matplotlib.pyplot as plt

img = cv2.imread('ad.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()
