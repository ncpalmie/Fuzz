from PIL import Image
from typing import Tuple
import numpy as np
import random as rnd


def random_from_all(img: np.ndarray, times: int = 1) -> np.ndarray:
    """
    Accepts a numpy array representing an image and a number of times to perform
    the random operation. This operation replaces each pixel in the array with
    another random pixel somewhere else in the array.
    """
    rng = np.random.default_rng()
    flat_img = img.reshape(-1, 3)
    rng.shuffle(flat_img)
    return np.reshape(flat_img, (-1, img.shape[1], 3))


def randomize_cols(img: np.ndarray, times: int = 1) -> np.ndarray:
    """
    Accepts a numpy array representing an image and a number of times to perform
    the random operation. This operation shuffles the columns of pixels into a
    random order.
    """
    rng = np.random.default_rng()
    rng.shuffle(img, axis=1)
    return img


def randomize_rows(img: np.ndarray, times: int = 1) -> np.ndarray:
    """
    Accepts a numpy array representing an image and a number of times to perform
    the random operation. This operation shuffles the rows of pixels into a
    random order.
    """
    rng = np.random.default_rng()
    rng.shuffle(img)
    return img


def melt(img: np.ndarray, sorted: bool = False) -> np.ndarray:
    """
    Accepts a numpy array representing an image and "melts" the image into
    groupings of similar pixels. If 'sorted' is set to True, the colors will
    be sorted by their RGB values in ascending order.
    """
    pixel_dict = {}
    for pixel in img.reshape(-1, 3):
        pix_tup = tuple(pixel)
        try:
            pixel_dict[pix_tup] = pixel_dict[pix_tup] + 1
        except KeyError:
            pixel_dict[pix_tup] = 1

    pixels = list(pixel_dict.keys())
    if sorted:
        pixels.sort()
    new_img = []
    for pixel in pixels:
        tmp_list = []
        for _ in range(0, pixel_dict[pixel]):
            tmp_list.append(np.asarray(pixel))
        new_img += tmp_list
    return np.asarray(new_img).reshape(-1, img.shape[1], 3)
