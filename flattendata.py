import numpy as np
from imagedata_NeoroScan import medical_train, medical_test



def flatten_data(image_data):
    flattened = []

    for label, class_img in enumerate(image_data):
        if class_img is None:
            continue

        for img in class_img:
            if img is None:
                continue

            flattened.append((img, label))

    return flattened


imgtrain = flatten_data(medical_train)
imgtest = flatten_data(medical_test)


