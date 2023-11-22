import numpy as np
from PIL import Image
from io import BytesIO
from urllib import request


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, resample=Image.Resampling.NEAREST)
    return img


def preprocess_input(img):
    X = np.array(img, dtype='float32')
    X = np.array([X])
    X /= 127.5
    X -= 1.
    return X