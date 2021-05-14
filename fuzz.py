from PIL import Image
import numpy as np
import manipulators

im = Image.open("vangogh.png")
pixels = np.array(im)

pixels = manipulators.randomize_cols(pixels)

im = Image.fromarray(pixels)
im.save("fuzzy_vangogh.png")
