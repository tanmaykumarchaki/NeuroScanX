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


# class imageconvert:
#     def __init__(self):
#         self.image = None
#         self.vectors = []
#         self.tensors = []
#         self.labels = []
    
#     def vectorimg_flat(self, image_var):
#         for class_group in image_var:
#             for img in class_group:
#                 self.image = img.convert('RGB')
#                 self.image_tensor = torch.from_numpy(np.array(self.image))
#                 self.image_vec = self.image_tensor.view(-1)
#                 self.vectors.append(self.image_vec)

#         return torch.stack(self.vectors)
    
#     def transformer(self, image_var, size=(224,224)):
#         transform = transforms.Compose([
#             transforms.Resize(size),
#             transforms.ToTensor()
#         ])

#         for labels , class_group in enumerate(image_var):
#             for img in class_group:
#                 self.image = img.convert('RGB')
#                 self.image_tensor = transform(self.image)
#                 self.tensors.append(self.image_tensor)
#                 self.labels.append(labels)

#         return torch.stack(self.tensors) , torch.tensor(self.labels)



# # print("Image Conversion Class =", dis.dis(imageconvert))

 
def meta_data(var):
    for class_id, image_list in enumerate(var):
        for img_indx , img in enumerate(image_list):
            metadata = []


            w, h = img.size
            mode = img.mode
            asp_ratio = w/h

            record = {
                "class_id": class_id,
                "image_index": img_indx,
                "width": w,
                "height": h,
                "mode": mode,
                "aspect_ratio": asp_ratio
            }

            metadata.append(record)

            
print("Meta Data Parsing Function :", dis.dis(meta_data))

        
def ten_2_df(data, labels, split):
    import pandas as pd 
    import numpy as np
    import torch

    tensor_stack = torch.stack(data)

    tensor_stack = tensor_stack.view(tensor_stack.size(0), -1)

    t =  tensor_stack.detach().cpu().numpy()

  
    

    #   tensor_stack = torch.stack(tensor)
    #   tensor_stack = tensor_stack.view(tensor_stack.size(0), -1)

    #   t = tensor_stack.detach().cpu().numpy()


    # elif isinstance(tensor, list):

    #     data = [torch.tensor(x) 
    #             if isinstance(x, torch.Tensor) 
    #             else x for x in tensor]
        
    #     tensor_stack = torch.stack(data)

    # elif isinstance(tensor, np.ndarray):
    #     tensor_stack = torch.from_numpy(tensor)

    # else:
    #     try:
    #         tensor_stack = torch.stack(list(tensor))
    #     except:
    #         raise TypeError(F"Unsupported Tensor Type: {type(tensor)}")
        

    # tensor_stack = tensor_stack.view(tensor_stack.size(0), -1)

    # t = tensor_stack.detach().cpu().numpy()
    
    feat_cols = [f"feat_{i}" for i in range(t.shape[1])]
    df = pd.DataFrame(t, columns=feat_cols)

    df["label"] = labels
    df["type"] = split

    return df
print("Tensor to DataFrame Function:", dis.dis(ten_2_df))

# def extract_feature(loader, model):
#     model.eval()
#     features = []

#     with torch.no_grad():
#         for images in loader:
#             images = images.to(loader)

#             output = model(images)

#             output = output.view(output.size(0), -1)

#             features.append(output.cpu())

#     return torch.cat(features)

# print("Feature Extraction function =", dis.dis(extract_feature))

import torch

def norm_ts(var):

    print("Incoming Type:", type(var))

    # -------------------------
    # Case 1: Already Tensor
    # -------------------------
    if isinstance(var, torch.Tensor):
        print("Data is already a Tensor")
        return var.view(var.size(0), -1)

    # -------------------------
    # Case 2: List
    # -------------------------
    elif isinstance(var, list):

        if len(var) == 0:
            raise ValueError("List is empty")

        print("Element type inside list:", type(var[0]))

        # Case A: List of Tensors
        if isinstance(var[0], torch.Tensor):
            print("List contains Tensors. Stacking...")
            stacked = torch.stack(var)

        # Case B: List of Sequential (Wrong)
        elif isinstance(var[0], torch.nn.Sequential):
            raise ValueError("List contains Sequential models, not Tensor outputs!")

        else:
            raise ValueError("Unsupported element type inside list")

        return stacked.view(stacked.size(0), -1)

    # -------------------------
    # Case 3: Unsupported Type
    # -------------------------
    else:
        raise ValueError("Unsupported data type passed.")
    
print("Normaliser To Tensor:",dis.dis(norm_ts))
        

def seq_2_df(seq_obj, labels, split):
    import pandas as pd 
    import numpy as np
    import torch


    if isinstance(seq_obj, torch.nn.Sequential):
        raise ValueError("Sequential Objects are not supported for conversion !")
    
    if isinstance(seq_obj, list):
        tensor_stack = torch.stack(seq_obj)

    elif isinstance(seq_obj, torch.Tensor):
        tensor_stack = seq_obj

    else:
        raise ValueError("Unsupported data type")
    
    tensor_stack = tensor_stack.view(tensor_stack.size(0), -1)

    t = tensor_stack.detach().cpu().numpy()

    feat_cols = [f"feat_{i}" for i in range(t.shape[1])]

    df = pd.DataFrame(t, columns= feat_cols)
    df["label"] = labels
    df["split"] = split

    return df

print("Sequential To DataFrame =", dis.dis(seq_2_df))


def clean_label(label):
    label = label.lower()  #Normalize Case
    label = label.replace("train","")
    label = label.replace("test","")
    label = label.strip()  #remove extra spaces

    return label

print("Clean Label Function = ",dis.dis(clean_label))