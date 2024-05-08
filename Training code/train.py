from ultralytics import YOLO

# Load a model
model = YOLO("yolov8m.yaml")  # build a new model from scratch

# Use the model
model.train(data="coco8.yaml", epochs=3)  # train the model
