import numpy as np
from imagedata_NeoroScan import medical_train, medical_test

def flatten_data(image_data):
    flattened = []
    for data in image_data:
        for img in data:
            img_array = np.array(img)
            flattened.append(img_array.flatten())

imgtrain = flatten_data(medical_train)
imgtest = flatten_data(medical_test)

print(f"Flattened Training Data Shape: {np.array(imgtrain).shape}")
print(f"Flattened Testing Data Shape: {np.array(imgtest).shape}")
