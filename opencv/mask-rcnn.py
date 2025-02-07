import cv2
import numpy as np

# Load the pre-trained Mask R-CNN model
model_weights = "/home/sinhurry/mywerks/muyOpenCv/opencv/files/frozen_inference_graph.pb"
model_config = "/home/sinhurry/mywerks/muyOpenCv/opencv/files/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt"

net = cv2.dnn.readNetFromTensorflow(model_weights, model_config)

# Load class labels from COCO dataset
class_names = {1: "person", 2: "bicycle", 3: "car", 4: "motorcycle", 5: "airplane",
               6: "bus", 7: "train", 8: "truck", 9: "boat", 10: "traffic light"}

# Load an image
image = cv2.imread("/home/sinhurry/mywerks/muyOpenCv/opencv/files/cats.jpeg")
height, width, _ = image.shape

# Convert image to blob
blob = cv2.dnn.blobFromImage(image, swapRB=True, crop=False)
net.setInput(blob)

# Forward pass through the network
boxes, masks = net.forward(["detection_out_final", "detection_masks"])

# Loop through detections
num_detections = boxes.shape[2]
for i in range(num_detections):
    box = boxes[0, 0, i]
    score = box[2]

    if score > 0.5:  # Confidence threshold
        class_id = int(box[1])  # Get class ID
        label = class_names.get(class_id, "Unknown")

        # Get box coordinates
        x1 = int(box[3] * width)
        y1 = int(box[4] * height)
        x2 = int(box[5] * width)
        y2 = int(box[6] * height)

        # Draw bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f"{label}: {score:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Get the mask
        mask = masks[i, class_id]
        mask = cv2.resize(mask, (x2 - x1, y2 - y1))

        # Apply threshold to create a binary mask
        mask = (mask > 0.5).astype(np.uint8)

        # Create a colored mask overlay
        colored_mask = np.zeros_like(image[y1:y2, x1:x2])
        colored_mask[:, :, 1] = 255  # Green color for the mask

        # Blend mask with image
        mask_indices = mask == 1
        image[y1:y2, x1:x2][mask_indices] = (
            0.6 * image[y1:y2, x1:x2][mask_indices] + 0.4 * colored_mask[mask_indices]
        )

# Show the output image
cv2.imshow("Mask R-CNN Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
