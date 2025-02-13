import cv2

# Load a pre-trained model (e.g., MobileNet)
net = cv2.dnn.readNetFromCaffe('mobilenet_deploy.prototxt', 'mobilenet.caffemodel')

# Read an image
image = cv2.imread('image.jpg')

# Convert image to blob (required format for deep learning models)
blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(224, 224), mean=(104, 117, 123))

# Set the input to the network
net.setInput(blob)

# Run inference
output = net.forward()
print('+++ output ', output)