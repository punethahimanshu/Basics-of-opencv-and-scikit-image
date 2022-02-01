
"""
Manual and auto thresholding
@author: HIMANSHU

"""
import cv2
from skimage import io
from matplotlib import pyplot as plt

img = cv2.imread("Images/Osteosarcoma_01.tif", 1) # BGR image because of opencv 
#             (1104,1376,3)=(y,x,channels (BGR))

#img_skimage = io.imread("Images/Osteosarcoma_01.tif") # RGB image
#plt.imshow(img_skimage)
plt.imshow(img)

###############################################################
# Separate blue channels as they contain nuclei pixels (DAPI)

blue_channel = img[:,:,0] #[all x, all y, only blue channel]
plt.imshow(blue_channel, cmap = 'gray')
plt.hist(blue_channel.flat, bins = 100, range = (0,120))

###############################################################

# Manual thresholding by setting threshold values to numpy array
# After thresholding we will get a binary image
background = (blue_channel <= 40)
nuclei = (blue_channel > 40)
plt.imshow(nuclei, cmap ='gray')   # Thresholding imaage of nuclei



# Using opencv to manual threshold
# All pixel values above 40 will have pixel value 255
# same as above mentioned method

ret1,thresh1 =cv2.threshold(blue_channel, 40, 255,cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap ='gray')   # Thresholding imaage of nuclei

# Where, ret1 = Threshold value
#        thresh1 = All the pixels values after thresholding or Output

#################################################################

# What if we don't know the exact value of threshold at 40 (just say) after histogram
# we use a automatic method called OTSU

ret2,thresh2 =cv2.threshold(blue_channel, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# so we get a new threshold value ret2 = 50

plt.imshow(thresh2, cmap ='gray')

#################################################################
import numpy as np

regions1 = np.digitize(blue_channel, bins=np.array([ret2]))
plt.imshow(regions1)

















