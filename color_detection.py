import cv2
import numpy as np


def get_hsv_bounds(rgb_color):
    color = np.uint8([[rgb_color]]) #rgb -> hsv
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)[0][0]


   
    lower_bound = np.array([hsv_color[0] - 10, 100, 100])
    upper_bound = np.array([hsv_color[0] + 10, 255, 255])


    return lower_bound, upper_bound


# user se input
r = int(input("Enter the R value (0-255): "))
g = int(input("Enter the G value (0-255): "))
b = int(input("Enter the B value (0-255): "))


# Get the HSV bounds for the selected color
lower_hsv, upper_hsv = get_hsv_bounds([b, g, r])  # OpenCV uses BGR format


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break


    # Convert the frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv_frame, lower_hsv, upper_hsv)


    # masking
    result = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow("Detected Color", result)


    if cv2.waitKey(1) & 0xFF == 27: #esc to exit
        break


cap.release()
cv2.destroyAllWindows()
