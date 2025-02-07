import cv2

# Load the pre-trained Mask R-CNN model
model_weights = "/home/sinhurry/mywerks/muyOpenCv/opencv/files/frozen_inference_graph.pb"
model_config = "/home/sinhurry/mywerks/muyOpenCv/opencv/files/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt"
# Load the pre-trained Mask R-CNN model
net = cv2.dnn.readNetFromTensorflow(
    model_weights,
    model_config
)

# Check if the model is loaded
if net.empty():
    print("Error loading Mask R-CNN model!")
else:
    print("Mask R-CNN model loaded successfully.")
