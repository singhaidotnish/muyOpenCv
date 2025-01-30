import cv2


def main():
    image_name = '/home/sinhurry/Downloads/ffmpeg-images/pexels-pixabay-357159.jpg'
    new_image = '/home/sinhurry/Downloads/ffmpeg-images/pexels-pixabay-357159_new_image.jpg'
    image = cv2.imread(image_name)

    # Save as PNG
    cv2.imwrite(new_image, image)

    # cv2.imshow("new image", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Image saved successfully!")


if __name__ == '__main__':
    main()