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


class imageconvert:
    def __init__(self):
        self.image = None
        self.vectors = []
        self.tensors = []
        self.labels = []
    
    def vectorimg_flat(self, image_var):
        for class_group in image_var:
            for img in class_group:
                self.image = img.convert('RGB')
                self.image_tensor = torch.from_numpy(np.array(self.image))
                self.image_vec = self.image_tensor.view(-1)
                self.vectors.append(self.image_vec)

        return torch.stack(self.vectors)
    
    def transformer(self, image_var, size=(224,224)):
        transform = transforms.Compose([
            transforms.Resize(size),
            transforms.ToTensor()
        ])

        for labels , class_group in enumerate(image_var):
            for img in class_group:
                self.image = img.convert('RGB')
                self.image_tensor = transform(self.image)
                self.tensors.append(self.image_tensor)
                self.labels.append(labels)

        return torch.stack(self.tensors) , torch.tensor(self.labels)
    

print("Image Conversion Class =", dis.dis(imageconvert))

 

