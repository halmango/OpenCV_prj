import cv2

image = "./images/hamhamday.jpg"
cv_image = cv2.imread(image, cv2.IMREAD_COLOR)
cv2.imshow("First OpenCV", cv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
