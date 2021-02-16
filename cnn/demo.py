import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import glob


datasets = []
files = glob.glob("source/like/claire45.jpg")
for file in files:
    image = cv2.imread(file)
    print(image.shape)
    img = cv2.resize(image, (600,400), interpolation = cv2.INTER_AREA)
    cv2.imshow("test",img)
    cv2.waitKey(0)