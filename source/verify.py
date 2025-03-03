import numpy as np 
import cv2 
import torch 
from ultralytics import YOLO  # Import YOLO from ultralytics
import os
import onnxruntime as ort


onnx_model = YOLO(r'{your_path}\\best.onnx')

## Process the outputs according to your model's specific output format
images_path = r'{your_path}\dataset\obdet_v23_1\train\images'

for filename in os.listdir(images_path):
    if filename.endswith('.jpg'):
        image = os.path.join(images_path, filename)
        image = cv2.imread(image)
      # Resize image to 640x640 (or the size your model expects
        results = onnx_model(image)
        for result in results:  # Iterate through the list of Results objects
            boxes = result.boxes  # Bounding boxes
            if boxes is not None and len(boxes) > 0:
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]  # Get the bounding box coordinates
                    conf = box.conf[0]  # Get the confidence score
                    cls = box.cls[0]  # Get the class ID
                    
                    # Convert tensor values to Python types
                    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
                    conf = float(conf)
                    cls = int(cls)
                    
                    # Draw bounding box and label on the image
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    label = f"{onnx_model.names[cls]} {conf:.2f}"
                    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Display or save the annotated image
            cv2.imshow("Result", image)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()


#     boxes = result.boxes  # Bounding boxes



