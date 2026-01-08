import numpy as np
import torch
import PIL.Image as img
import dis

print(torch.__version__)
print(np.__version__)
print(img.__version__)

#image into metadata using torch and PIL

def img_metadata(image_path):
    image = img.open(image_path) # opening images using PIL
    image_tensor = torch.from_numpy(np.array(image)) # converting image to tensor using torch
    metadata = {
        "format": image.format,
        "mode": image.mode,
        "size": image.size,
        "tensor_shape": image_tensor.shape,
        "image_tensor_": image_tensor
    } # storing metadata in a dictionary
    return metadata

print(dis.dis(img_metadata))

#converting image to tensor using torch and PIL

def tensorimg(image_variable):
    image = img.open(image_variable)
    image_tensor = torch.from_numpy(np.array(image))
    return image_tensor

print(dis.dis(tensorimg))
