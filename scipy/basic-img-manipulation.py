from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import imageio

#open img file and stores as np array
img = imageio.imread('../test.jpg')

print("Image shape:", img.shape, "image type:", img.dtype)

plt.imshow(img, cmap="gray")
plt.show()

imageio.imwrite('test2.png', img)

print("Mean:", img.mean())
print("Min:", img.min())
print("Max:", img.max())

#apply rotation transformation
f = np.flipud(img)
plt.imshow(f)
plt.show()

#smooth image with gaussian filter
g = ndimage.gaussian_filter(img, sigma=7)
h = ndimage.gaussian_filter(img, sigma=11)
plt.imshow(g)
plt.show()
plt.imshow(h)
plt.show()