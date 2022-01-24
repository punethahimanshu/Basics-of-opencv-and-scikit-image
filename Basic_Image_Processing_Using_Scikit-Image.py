# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:17:44 2022

@author: HIMANSHU
"""
from matplotlib import pyplot as plt

from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean

img = io.imread("Images/Osteosarcoma_01.tif", as_gray=True)

# Rescaling the Image

img_rescaled = rescale(img, 1.0/4.0, anti_aliasing= False)

# rescaling factor = 25%

plt.imshow(img_rescaled, cmap= 'gray')

# Resizing Image

img_resized = resize(img, (200,200), anti_aliasing = True)
plt.imshow(img_resized, cmap= 'gray')

# Image downscaled

img_downscaled= downscale_local_mean(img, (4, 3))
plt.imshow(img_downscaled, cmap= 'gray')

# subplot for original, rescaled, resized and downscaled images

fig = plt.figure(figsize = (10,10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap = 'gray')
ax1.title.set_text('Original Image')

ax1 = fig.add_subplot(2,2,2)
ax1.imshow(img_rescaled, cmap = 'gray')
ax1.title.set_text('Rescaled Image')

ax1 = fig.add_subplot(2,2,3)
ax1.imshow(img_resized, cmap = 'gray')
ax1.title.set_text('Resized Image')

ax1 = fig.add_subplot(2,2,4)
ax1.imshow(img_downscaled, cmap = 'gray')
ax1.title.set_text('Downscaled Image')

######################################################################

# Applying filters to Images

from skimage import io
from skimage.filters import gaussian, sobel

img1 = io.imread("Images/Osteosarcoma_01_25Sigma_noise.tif")
plt.imshow(img1)

gaussian_using_skimage= gaussian(img1, sigma=2, mode='constant', cval=0.0)
plt.imshow(gaussian_using_skimage)

img_gray = io.imread("Images/Osteosarcoma_01.tif", as_gray=True)
sobel_img = sobel(img_gray)  # sobel filter for edge detection
plt.imshow(sobel_img, cmap= 'gray')


