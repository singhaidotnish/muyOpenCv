import cv2
import os

# Parameters
label = "dog"  # Change label for different categories
num_images = 20  # Number of images to capture
delay = 1  # Time delay in seconds between captures

# Create a folder to save images
SAVE_PATH = f"dataset/{label}"
os.makedirs(SAVE_PATH, exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(0)  # 0 for the default webcam

if not cap.isOpened():
    print("❌ Error: Could not open webcam!")
    exit()

print("📸 Press SPACE to capture an image. Press ESC to exit.")

image_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Failed to capture image.")
        break

    # Show the webcam feed
    cv2.imshow("Webcam - Press SPACE to Capture", frame)

    # Wait for keypress
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC key to exit
        break
    elif key == 32:  # SPACE key to capture
        image_path = os.path.join(SAVE_PATH, f"{label}_{image_count}.jpg")
        cv2.imwrite(image_path, frame)
        print(f"✅ Image saved: {image_path}")
        image_count += 1

        if image_count >= num_images:
            print("🎉 Image capture complete!")
            break

# Release the webcam
cap.release()
cv2.destroyAllWindows()
