import os
import random
import shutil

# assume all 900 images are in a single directory called 'images'
image_dir = 'augmented_data'
image_files = os.listdir(image_dir)

# shuffle the list of image files
random.shuffle(image_files)

# split the list into three parts: 720 for train, 90 for val, and 90 for test
train_files = image_files[:720]
val_files = image_files[720:810]
test_files = image_files[810:]

# create the three folders if they don't exist
for folder in ['train', 'val', 'test']:
    if not os.path.exists(folder):
        os.makedirs(folder)

# move the images to their respective folders
for file in train_files:
    shutil.move(os.path.join(image_dir, file), 'train')
for file in val_files:
    shutil.move(os.path.join(image_dir, file), 'val')
for file in test_files:
    shutil.move(os.path.join(image_dir, file), 'test')