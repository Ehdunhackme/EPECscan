import os
import random
import shutil

# assume all 900 images and labels are in a single directory called 'images' and 'labels'
image_dir = os.path.join(os.getcwd(),"Training Data", "augmented_data")
label_dir = os.path.join(os.getcwd(),"Training Data", "labels")
image_files = os.listdir(image_dir)
label_files = os.listdir(label_dir)

# shuffle the list of image files
random.shuffle(image_files)

# split the list into three parts: 720 for train, 90 for val, and 90 for test
train_files = image_files[:720]
val_files = image_files[720:810]
test_files = image_files[810:]

# create the three folders if they don't exist
for folder in ['train', 'val', 'test']:
    if not os.path.exists(os.path.join('Training Data', folder)):
        os.makedirs(os.path.join('Training Data', folder))
        os.makedirs(os.path.join('Training Data', folder, 'images'))
        os.makedirs(os.path.join('Training Data', folder, 'labels'))

# move the images and labels to their respective folders
for file in train_files:
    shutil.move(os.path.join(image_dir, file), os.path.join('Training Data', 'train', 'images'))
    shutil.move(os.path.join(label_dir, file.replace('.png', '.txt')), os.path.join('Training Data', 'train', 'labels'))
for file in val_files:
    shutil.move(os.path.join(image_dir, file), os.path.join('Training Data', 'val', 'images'))
    shutil.move(os.path.join(label_dir, file.replace('.png', '.txt')), os.path.join('Training Data', 'val', 'labels'))
for file in test_files:
    shutil.move(os.path.join(image_dir, file), os.path.join('Training Data', 'test', 'images'))
    shutil.move(os.path.join(label_dir, file.replace('.png', '.txt')), os.path.join('Training Data', 'test', 'labels'))

print("Data splitting finished.")