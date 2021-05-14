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
