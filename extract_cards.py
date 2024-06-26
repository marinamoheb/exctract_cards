import cv2
import numpy as np

image_path="bc4.jpeg"
image=cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
ret, thresholded=cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)

edged = cv2.Canny(blur, 30, 200, apertureSize=5)
# _, threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)
#combo= np.concatenate((image, gray), axis=1)
#cv2.imshow("Image", image)

# cv2.imshow("Gray", gray)
#cv2.imshow("Blurred", blur)
#cv2.imshow("Thresholded", thresholded)

cv2.imshow("Edged", edged)
cv2.waitKey(0)
print("closing")
cv2.destroyAllWindows()
