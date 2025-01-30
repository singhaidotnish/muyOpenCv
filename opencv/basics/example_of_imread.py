import cv2


def main():
    file_name = '/home/sinhurry/Downloads/ffmpeg-images/pexels-jvdm-1564839.jpg'
    image = cv2.imread(file_name, cv2.IMREAD_COLOR)
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    image = cv2.imread(file_name, cv2.IMREAD_COLOR_RGB)
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    image = cv2.imread(file_name, cv2.IMREAD_COLOR_BGR)
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    image = cv2.imread(file_name, cv2.IMREAD_REDUCED_COLOR_2)
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    image = cv2.imread(file_name, cv2.IMREAD_REDUCED_COLOR_4)
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    image = cv2.imread(file_name, cv2.IMREAD_REDUCED_COLOR_8)
    cv2.imshow("Display", image)
    cv2.waitKey(0)

    image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    image = cv2.imread(file_name, cv2.IMREAD_REDUCED_GRAYSCALE_2)
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    image = cv2.imread(file_name, cv2.IMREAD_REDUCED_GRAYSCALE_4)
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    image = cv2.imread(file_name, cv2.IMREAD_REDUCED_GRAYSCALE_8)
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    image = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Display", image)
    cv2.waitKey(0)

    try:
        image = cv2.imread("non_existing_file.jpg")
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print("Error: Image not found!")
    finally:
        print("Closing All")


if __name__ == '__main__':
    main()
