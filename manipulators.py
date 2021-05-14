from PIL import Image
from typing import Tuple
import numpy as np
import random


def randomize(img: np.ndarray, times: int) -> Tuple[int, ...]:
    """
    Accepts a numpy array representing an image and a number of times to perform
    the random operation. This operation replaces each pixel in the array with
    another random pixel somewhere else in the array.
    """
