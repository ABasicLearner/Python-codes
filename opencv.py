import cv2

cam = cv2.VideoCapture(0)
result, image = cam.read()

if result:
    cv2.imshow("Photo", image)
    cv2.imwrite('image.png', image)

    cv2.waitKey(10)
    cv2.destroyWindow("Image")

