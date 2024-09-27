import cv2
import numpy as np

color_ranges = {
    "red": ([0, 100, 100], [10, 255, 255]),
    "green": ([40, 100, 100], [80, 255, 255]),
    "blue": ([100, 100, 100], [140, 255, 255]),
    "yellow": ([20, 100, 100], [40, 255, 255]),
}

def get_hsv_bounds(color_name):
    return np.array(color_ranges[color_name][0]), np.array(color_ranges[color_name][1])

color_name = input("Enter a color (red, green, blue, yellow): ").strip().lower()

if color_name not in color_ranges:
    print("Color not recognized. Using red as default.")
    color_name = "red"

lower_hsv, upper_hsv = get_hsv_bounds(color_name)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, lower_hsv, upper_hsv)
    
    result = cv2.bitwise_and(frame, frame, mask=mask)
   
    grid_height = 480
    grid_width = 640
    grid = np.zeros((grid_height, grid_width, 3), dtype=np.uint8)

    if np.any(mask):  # Only fill if there's a detection
        y_indices, x_indices = np.where(mask > 0)
        for y, x in zip(y_indices, x_indices):
            grid[y % grid_height, x % grid_width] = frame[y, x]


    cv2.imshow("Detected Color Grid", grid)
    cv2.imshow("Original Frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # esc to exit
        break

cap.release()
cv2.destroyAllWindows()
