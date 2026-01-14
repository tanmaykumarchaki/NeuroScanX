import os 
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import random

valid_extentions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']


def load_images(folder_path):
    image_paths = []
    images = []

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder path {folder_path} does not found !")
    for filename in os.listdir(folder_path):
        ext = os.path.splitext(filename)[1].lower()
        if ext in valid_extentions:
            image_paths.append(os.path.join(folder_path, filename))

    print(f"Found {len(image_paths)}")

    for path in image_paths:
        try:
            img = Image.open(path).convert('RGB')
            images.append(img)
        except Exception as e:
            print(f"Failed to Load {path}: {e}")

    print(f"Successfully loaded {len(images)}")
    return images
 

glioma_tdir = r"C:\Users\Tanmay\OneDrive\Desktop\ML Project 2026\archive (1)\Train\Train\Glioma\images"
meningioma_tdir = r"C:\Users\Tanmay\OneDrive\Desktop\ML Project 2026\archive (1)\Train\Train\Meningioma\images"
non_tumor_tdir = r"C:\Users\Tanmay\OneDrive\Desktop\ML Project 2026\archive (1)\Train\Train\No Tumor\images"
pituitary_tdir = r"C:\Users\Tanmay\OneDrive\Desktop\ML Project 2026\archive (1)\Train\Train\Pituitary\images"

glioma_train = load_images(glioma_tdir)
meningioma_train = load_images(meningioma_tdir)
non_tumor_train = load_images(non_tumor_tdir)
pituitary_tdir = load_images(pituitary_tdir)

medical_train = [glioma_train, meningioma_train, non_tumor_train, pituitary_tdir]
print(f"Total Training Images: {sum(len(img) for img in medical_train)}")
print("All Training Images Loaded Successfully!")

glioma_tsdir =r"C:\Users\Tanmay\OneDrive\Desktop\ML Project 2026\archive (1)\test\test\Glioma\images"
meningioma_tsdir = r"C:\Users\Tanmay\OneDrive\Desktop\ML Project 2026\archive (1)\test\test\Meningioma\images"
non_tumor_tsdir = r"C:\Users\Tanmay\OneDrive\Desktop\ML Project 2026\archive (1)\test\test\No Tumor\images"
pituitary_tsdir = r"C:\Users\Tanmay\OneDrive\Desktop\ML Project 2026\archive (1)\test\test\Pituitary\images"

glioma_test = load_images(glioma_tsdir)
meningioma_test = load_images(meningioma_tsdir)
non_tumor_test = load_images(non_tumor_tsdir)
pituitary_test = load_images(pituitary_tsdir)


medical_train = [glioma_train, meningioma_train, non_tumor_train, pituitary_tdir]
print(f"Total Training Images: {sum(len(img) for img in medical_train)}")
print("All Training Images Loaded Successfully!")

medical_test = [glioma_test, meningioma_test, non_tumor_test, pituitary_test]
print(f"Total Testing Images: {sum(len(img) for img in medical_test)}")
print("All Testing Images loaded successfully!")

#Image Display 
def display_img(
        nested_variable,
        node_index = None,
        max_images = 10,
        figsize = (15,15)

):
    if node_index is not None:
        node = random.choice(nested_variable)
    else:
        node = nested_variable[node_index]

    images = random.sample(node, min(len(node), max_images))
    plt.figure(figsize= figsize)

    for idx , img in enumerate(images):
        plt.subplot(1 , len(images), idx + 1)

        if isinstance(img, Image.Image):
            plt.imshow(img)

        else:
            plt.imshow(img, Image.Image)

        plt.axis('off')

    plt.tight_layout()
    plt.show()



