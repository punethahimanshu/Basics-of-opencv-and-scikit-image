# -*- coding: utf-8 -*-
"""
@author: HIMANSHU
"""

"""
Unsharp mask

unsharpened image = original + amount * (original - blurred)

"""
from skimage import io, img_as_float
# from skimage.filters import unsharp_mask
from skimage.filters import gaussian

img = img_as_float(io.imread("Images/sandstone_blur_2sigma.tif", as_gray=True))
gaussian_img = gaussian(img, sigma = 2, mode ="constant", cval=0.0)

img2 = (img - gaussian_img)*2
img3 = img + img2

from matplotlib import pyplot as plt
plt.imshow(img3, cmap='gray')



# Second Method Using Builtin function unsharp_mask() to --> sharpen the images

from skimage import io
from skimage.filters import unsharp_mask

img = io.imread("Images/sandstone_blur_2sigma.tif")

# Radius defines the degree of blurring
# Amount defines the multiplication factor for original-blurred image

unsharped_img = unsharp_mask(img, radius=3, amount=2)

from matplotlib import pyplot as plt

fig = plt.figure(figsize = (12,12))
ax1 = fig.add_subplot(1,2,1) 
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax1 = fig.add_subplot(1,2,2) 
ax1.imshow(unsharped_img, cmap='gray')
ax1.title.set_text('Unsharpned Image')

plt.show()



