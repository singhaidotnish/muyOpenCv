import cv2

def main():
    image_name = '/home/sinhurry/Downloads/ffmpeg-images/pexels-pixabay-357159_new_image.jpg'
    image = cv2.imread(image_name)

    # Get pixel value at (x=50, y=100)
    b, g, r = image[100, 50]

    print(f"Blue: {b}, Green: {g}, Red: {r}")

    b, g, r = image[1000, 590]

    print(f"Blue: {b}, Green: {g}, Red: {r}")

    b, g, r = image[10, 500]

    print(f"Blue: {b}, Green: {g}, Red: {r}")


if __name__ == '__main__':
    main()
