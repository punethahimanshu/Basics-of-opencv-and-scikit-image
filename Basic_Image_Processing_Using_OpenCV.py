# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:36:43 2022

@author: HIMANSHU
"""
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Images/RGB.png", 1)
plt.imshow(img) # color is BGR not RGB

#  Resizing the Images

resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Original Pic", img)
cv2.imshow("Resized Pic", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


gray_img = cv2.imread("Images/RGBY.png", 0) # 0 means gray image, 1 means color
plt.imshow(gray_img)   # This image is BGR not RGB

color_img= cv2.imread("Images/RGBY.png", 1) # color is BGR not RGB, 1 means color image
plt.imshow(color_img)

print(gray_img.shape) # (194,259)
print(color_img.shape) #(194,259,3)

# Spliting specific pixel from the Image

print("Top left Pixel", color_img[0,0]) # [B G R] = [0 255 0] , match with orignial color jpg image
print("Top Right Pixel", color_img[0,258]) # [B G R] = [0 0 255]
print("Bottom left Pixel", color_img[193,0]) # [B G R] = [255 0 0]
print("Bottom Right Pixel", color_img[193,258]) # [B G R] = [0 255 255]

# Spliting the channels with ist method (Long way)

Blue = color_img[:,:,0] # show only blue pic, 0 (BGR SO B=0 Channel)
Green = color_img[:,:,1]
Red = color_img[:,:,2]

cv2.imshow("Blue Pic", Blue)
cv2.imshow("Green Pic", Green)
cv2.imshow("Red Pic", Red)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Split the channels with builtin functions

b,g,r = cv2.split(color_img)
cv2.imshow("Blue Pic", b)
cv2.imshow("Green Pic", g)
cv2.imshow("Red Pic", r)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Merging the channel again
img_merged = cv2.merge((b,g,r))
cv2.imshow("Merged Pic", img_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Edge detection with the help of builtin function canny()

import cv2

pic = cv2.imread("Images/Osteosarcoma_01.tif", 0)

edges = cv2.Canny(pic, 100, 200)
cv2.imshow("Original Pic", pic)
cv2.imshow("Canny Pic", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


