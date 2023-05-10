import win32api
import cv2

from os import path

def show_image(imgName, winName, *grey):
    if grey[0] == "grey":
        grey_image = cv2.cvtColor(imgName, cv2.COLOR_BGR2GRAY)
        imgName = grey_image

    cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow(winName, 1000, 30)
    cv2.imshow(winName, imgName)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    image_file = "./images/hamhamday.jpg"

    if path.exists(image_file):
        image = cv2.imread(image_file, cv2.IMREAD_COLOR)
        show_image(image, "Color Image", None)
        show_image(image, "Grey Image", "grey")
    else:
        win32api.MessageBox(0, "이미지가 없습니다..", "ERROR", 16)
