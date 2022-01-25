# -*- coding: utf-8 -*-
"""
Bilateral Filter

@author: HIMANSHU
"""
import cv2
img_gaussian_noise = cv2.imread("Images/gaussian filter/Osteosarcoma_01_25Sigma_noise.tif", 0)

img = img_gaussian_noise

bilateral_using_cv2 = cv2.bilateralFilter(img, 5, 20, 100, borderType = cv2.BORDER_CONSTANT)

# d = diameter of each pixel neighborhood used during filtering
# sigmaColor = Sigma of gray/color space
# sigmaSpace = Large value means farther pixels infulence each other


# you can also use skimage for bilateral filter
#from skimage.restoration import denoise_bilateral
#bilateral_using_skimage = denoise_bilateral(img, sigma_color=0.05, sigma_spatial=15, 
                                           #multichannel=False)

cv2.imshow("Original Image with noise", img)
cv2.imshow(" cv2 Biletral Filtered Image",bilateral_using_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
