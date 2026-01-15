import numpy as np
import torch
import torchvision.transforms as transforms
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

print("Image MetaData Function ",dis.dis(img_metadata))

#converting image to tensor using torch and PIL

def tensorimg(image_variable):
    image = img.open(image_variable)
    image_tensor = torch.from_numpy(np.array(image))
    return image_tensor

print("Tensoring Image Function",dis.dis(tensorimg))

def structure_img(obj , level = 0):
    indent = "  " * level
    print(f"{indent}Type: {type(obj)}")

    if isinstance(obj , (list, tuple)) and len(obj) > 0:
        print(f"{indent}Lenght: {len(obj)}")
        structure_img(obj[0], level + 1)

    elif isinstance(obj, dict):
        first_key = next(iter(obj))
        print(f"{indent}Key Type: {type(first_key)}")
        structure_img(obj[first_key], level + 1)

print("Structuring Image function =", dis.dis(structure_img))


def vectorimg(image_list):
    vectors = []

    transform = transforms.Compose([
        transforms.Resize((128, 128)), # Resize the images into 128 x 128
        transform.ToTensor()
    ])


    for _img_ in image_list:
        
        _img_ = img.open(_img_).convert('RGB') 
        tensor_img = torch.from_numpy(np.array(_img_))
        vectors.append(tensor_img)

        for i in vectors:
            vectors =[i.view(-1) for i in vectors]
            vector_tensor = torch.stack(vectors) # Stacking all vectors into a single tensor 

        return vector_tensor

print("Vectorizing Image Function =", dis.dis(vectorimg))