import cv2


def main():
    image_name = r'/home/sinhurry/Downloads/ffmpeg-images/pexels-matthias-oben-output_320x240.png'
    image = cv2.imread(image_name)

    # Convert to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv_image)
    cv2.waitKey(0)

    # Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray_image)
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    cv2.imshow("COLOR_BGR2YCrCb", gray_image)
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLOR_YCrCb2BGR)
    cv2.imshow("COLOR_YCrCb2BGR", gray_image)
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLORMAP_WINTER)
    cv2.imshow("COLORMAP_WINTER", gray_image)
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLORMAP_AUTUMN)
    cv2.imshow("COLORMAP_AUTUMN", gray_image)
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLORMAP_MAGMA)
    cv2.imshow("COLORMAP_MAGMA", gray_image)
    cv2.waitKey(0)


    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()