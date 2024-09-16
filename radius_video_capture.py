import cv2
import numpy as np


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale to reduce noise
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)  # aur zyda noise reduction


    # Detect circles in the blurred grayscale frame
    circles = cv2.HoughCircles(gray_blurred,
                               cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                               param1=50, param2=30, minRadius=15, maxRadius=40)


    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")


        for (x, y, r) in circles:
            print(f"Circle detected: Center = ({x}, {y}), Radius = {r}")  # Print the center and radius
           
            # Draw the circle on the frame
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)  
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


            # Display the radius on the frame
            cv2.putText(frame, f"Radius: {r}", (x - 50, y - r - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)


   
    cv2.imshow('Webcam Circle Detection', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break


cap.release()
cv2.destroyAllWindows()
