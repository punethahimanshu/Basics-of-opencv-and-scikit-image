# -*- coding: utf-8 -*-
"""
@author: HIMANSHU
"""

import cv2
from skimage.filters import median

# Need 8 bit images (Arrays) not float

img_gaussian_noise = cv2.imread("Images/gaussian filter/Osteosarcoma_01_25Sigma_noise.tif", 0)

img_salt_pepper_noise =cv2.imread("Images/gaussian filter/Osteosarcoma_01_8bit_salt_pepper.tif",0)

#img1 = img_gaussian_noise
img2 = img_salt_pepper_noise

#median_using_cv2 = cv2.medianBlur(img2, 3)

from skimage.morphology import disk

median_using_skimage = median(img2, disk(3), mode='constant', cval=0.0)



cv2.imshow("Original Noisy", img2)
#cv2.imshow("Denoising with OpenCV", median_using_cv2)
cv2.imshow("Denoising with skimage", median_using_skimage)

cv2.waitKey(0)
cv2.destroyAllWindows()