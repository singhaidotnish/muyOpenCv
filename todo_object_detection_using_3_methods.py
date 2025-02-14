Object detection using OpenCV is typically done using techniques such as Haar cascades, YOLO (You Only Look Once), SSD (Single Shot MultiBox Detector), and Faster R-CNN. OpenCV provides built-in functions for detecting objects in images and videos.

Steps for Object Detection Using OpenCV

1. Install Dependencies

pip install opencv-python numpy


2. Load an Image or Video
OpenCV can process images, videos, or live camera feeds.


3. Choose a Detection Method

Haar Cascades (Good for face/object detection)

YOLO (Real-time object detection)

SSD & Faster R-CNN (More accurate deep learning models)





---

Method 1: Using Haar Cascades (Pre-trained Model)

Haar cascades are XML files trained to detect objects.

Example: Face Detection

import cv2

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load image
img = cv2.imread('face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw bounding boxes
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Show image
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


---

Method 2: Using YOLO for Object Detection

YOLO is a real-time object detection model.

Steps to Use YOLO

1. Download YOLO weights and configuration files.


2. Load the model into OpenCV.


3. Process the image and display results.



Example: YOLO Object Detection

import cv2
import numpy as np

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load COCO names (for class labels)
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load Image
img = cv2.imread("image.jpg")
height, width, channels = img.shape

# Prepare the image for YOLO
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), swapRB=True, crop=False)
net.setInput(blob)

# Get output layers
layer_names = net.getUnconnectedOutLayersNames()
outs = net.forward(layer_names)

# Extracting information
class_ids, confidences, boxes = [], [], []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x, center_y, w, h = (detection[:4] * [width, height, width, height]).astype("int")
            x, y = int(center_x - w / 2), int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply Non-Maximum Suppression (NMS)
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
for i in indices.flatten():
    x, y, w, h = boxes[i]
    label = f"{classes[class_ids[i]]}: {confidences[i]:.2f}"
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show image
cv2.imshow("Object Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
