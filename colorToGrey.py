import cv2

image = "./images/hamhamday.jpg"
color_image = cv2.imread(image, cv2.IMREAD_COLOR)
cv2.imshow("Color Image", color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

grey_image= cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image", grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

