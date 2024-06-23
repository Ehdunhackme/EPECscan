import os
import time
import csv
import matplotlib.pyplot as plt
from matplotlib import rcParams
from PIL import Image
from ultralytics import YOLO
import torch
import seaborn as sns

# Configuration
DEVICE = torch.device('cpu')
MODEL_PATH = r"C:\Users\dunli\Documents\STSY-project-main\Model Training\runs\detect\train16\weights\best.pt"
TEST_DATA_DIR = r"C:\Users\dunli\Documents\STSY-project-main\Training Data\Original Data\test_images"
LOG_CSV_PATH = "log.csv"

# Load the YOLO model
model = YOLO(MODEL_PATH).to(DEVICE)

# Function to log results to CSV
def log_to_csv(data, file_path):
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Process images using YOLO model
def process_images_yolo(model, image_dir, device, log_path):
    list_of_times = []
    log_data = []

    for image_file in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_file)
        print(f"Processing {image_path}")

        start_time = time.time()
        results = model(image_path)
        time_taken = time.time() - start_time
        list_of_times.append(time_taken)

        print("Time taken:", time_taken)

        # If you do not want to display the images, comment out or remove this block
        # for result in results:
        #     result.show()  # This will display the image with the bounding boxes

        # Collect log data
        log_data.append([image_file, image_path, time_taken])

    log_to_csv(log_data, log_path)

    return list_of_times

# Plot histogram of processing times with KDE curve
def plot_histogram_with_kde(data, title):
    plt.figure(figsize=(10, 6))
    sns.histplot(data, bins=20, kde=True)
    plt.xlabel("Time taken (s)")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.show()

# Process and log times for local inference
local_times = process_images_yolo(model, TEST_DATA_DIR, DEVICE, LOG_CSV_PATH)

# Calculate statistics
mean_time = sum(local_times) / len(local_times)
max_time = max(local_times)
min_time = min(local_times)
median_time = sorted(local_times)[len(local_times) // 2]

# Print statistics
print("Inference Time Metrics")
print(f"Mean    {mean_time:.4f}")
print(f"Max     {max_time:.4f}")
print(f"Min     {min_time:.4f}")
print(f"Median  {median_time:.4f}")

# Plot the histogram with KDE curve
plot_histogram_with_kde(local_times, "Time Taken to Process Each Image (Local)")
