import os 
from PIL import Image

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
 

glioma_dir = r"C:\Users\Tanmay\OneDrive\Desktop\ML Project 2026\archive (1)\Train\Train\Glioma\images"
glioma_train = load_images(glioma_dir)