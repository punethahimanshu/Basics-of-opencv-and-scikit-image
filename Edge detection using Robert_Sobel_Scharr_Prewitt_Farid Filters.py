
"""
Edge Detection Filters: Robert, Sobel, Scharr, Prewitt & Farid

@author: HIMANSHU
"""
import cv2
img = cv2.imread("Images/sandstone.tif", 0)

# Edge detection

from skimage.filters import roberts, sobel, scharr, prewitt

roberts_img = roberts(img)
sobel_img = sobel(img)
scharr_img = scharr(img)
prewitt_img = prewitt(img)

cv2.imshow("Roberts", roberts_img)
cv2.imshow("Sobel", sobel_img)
cv2.imshow("Scharr", scharr_img)
cv2.imshow("Prewitt", prewitt_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
