from ultralytics import YOLO

# Load a model
model = YOLO("yolov8m.yaml")  # build a new model from scratch

# Use the model
model.train(data="config.yaml", batch = 8, imgsz = 640, epochs = 5, workers = 1)

# CHANGE THE PATH INSIDE OF config.yaml