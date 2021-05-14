from PIL import Image
import numpy as np

im = Image.open("vangogh.png")
pixels = np.array(im)

print(pixels)
print(type(pixels))
