import cv2


def main():
    image_name = '/home/sinhurry/Downloads/ffmpeg-images/pexels-pixabay-60611.jpg'
    image = cv2.imread(image_name)

    # Resize image
    resized_image = cv2.resize(image, (300, 200))

    cv2.imshow("Resized", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()
