import cv2

# Load a pre-trained model (e.g., MobileNet)
net = cv2.dnn.readNetFromCaffe('mobilenet_deploy.prototxt', 'mobilenet.caffemodel')
'''
This function facilitates the integration of Caffe models into OpenCV applications, enabling tasks such as image classification, object detection, and more.

    +-------------------------+----------------------------------------------------------------------------------+
    |  Loading Caffe Models   |    Caffe models are typically defined by two files                               |
    +-------------------------+----------------------------------------------------------------------------------+
    |        Parameter        |    Description                                                                   |
    +=========================+==================================================================================+
    |      Prototxt File      | Specifies the architecture of the neural network,                                | 
    |                         | detailing the layers and their configurations.                                   |
    +-------------------------+----------------------------------------------------------------------------------+
    |      Caffemodel File    | Contains the pre-trained weights of the network.                                 |
    |                         |                                                                                  |
    +-------------------------+----------------------------------------------------------------------------------+

'''
# Read an image
image = cv2.imread('image.jpg')

# Convert image to blob (required format for deep learning models)
blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(224, 224), mean=(104, 117, 123))
'''
blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(width, height), mean=(mean_R, mean_G, mean_B), swapRB=True, crop=False)
    +------------+----------------------------------------------------------------------------------+
       Parameter |    Description
    +============+==================================================================================+
         image   |    Input image (NumPy array).
    +------------+----------------------------------------------------------------------------------+
     scalefactor |    Multiplier for scaling pixel values (e.g., 1/255.0 for normalization).
    +------------+----------------------------------------------------------------------------------+
        size     |    Target size (width, height) for the network (e.g., (224, 224) for MobileNet).
    +------------+----------------------------------------------------------------------------------+
        mean     |    Mean subtraction values (e.g., (104, 117, 123) for ImageNet models).
    +------------+----------------------------------------------------------------------------------+
        swapRB   |    Boolean flag to swap Red and Blue channels (use True for RGB models).
    +------------+----------------------------------------------------------------------------------+
        crop     |    Whether to center crop the image.
    +------------+----------------------------------------------------------------------------------+
    The function cv2.dnn.blobFromImage in OpenCV is essential when using deep learning models for image processing. 
    It helps preprocess images before feeding them into neural networks, ensuring that they match the input format 
    required by pre-trained models (e.g., MobileNet, YOLO, SSD, etc.).
    When training or using deep learning models, images need to be normalized, resized, and properly formatted. This function automates those steps by:
    ✅ Resizing the image to match the model's expected input size.
    ✅ Normalizing pixel values (e.g., scaling from [0, 255] to [0, 1] or [-1, 1]).
    ✅ Reordering color channels (from BGR to RGB if required).
    ✅ Adding a batch dimension (making it suitable for batch processing).

    Without this function, you would have to manually perform these steps using NumPy or OpenCV
'''
# Set the input to the network
net.setInput(blob)

# Run inference
output = net.forward()
'''

In deep learning, performing a forward pass on a loaded model is crucial for several reasons:
    +----------------------------------+----------------------------------------------------------------------------------+
         Generating Predictions        | The forward pass processes input data through the neural network to produce 
                                       | predictions or outputs. This is essential for tasks such as classification, 
                                       | regression, and more.  - GEEKSFORGEEKS.ORG
    +----------------------------------+----------------------------------------------------------------------------------+
      Evaluating Model Performance     | By comparing the model's predictions against actual target values, we can compute 
                                       | metrics like accuracy or loss, which help assess how well the model performs on 
                                       | specific tasks.  - TOWARDSDATASCIENCE.COM
    +----------------------------------+----------------------------------------------------------------------------------+
      Facilitating Backpropagation     | In the training phase, the forward pass is the initial step that computes the
      During Training                  | output and loss. This loss is then used in the backward pass (backpropagation) 
                                       | to update the model's parameters, thereby minimizing errors over time. - D2L.AI
    +----------------------------------+----------------------------------------------------------------------------------+
        Ensuring Model Functionality   | Executing a forward pass helps verify that the model is correctly loaded and 
                                       | operational, ensuring that all components are functioning as intended.
    +----------------------------------+----------------------------------------------------------------------------------+

In summary, the forward pass is fundamental in both the training and inference stages of deep learning models, enabling 
them to process data, learn from it, and make informed predictions.
'''
print('+++ output ', output)