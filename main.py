import cv2
import numpy as np

color_map = {
    (0, 0, 255): 100,
    (0, 128, 255): 90,
    (0, 255, 255): 80,
    (0, 255, 0): 70,
    (255, 128, 0): 60,
    (255, 255, 0): 50,
    (255, 0, 0): 40
}

st = "danger"


def thermal_image(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply colormap for heat mapping
    heat_map = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    # Detect red pixels
    red_mask = cv2.inRange(heat_map, (0, 0, 200), (50, 50, 255))
    red_pixels = cv2.countNonZero(red_mask)

    return heat_map, red_pixels


# Capture video from laptop's camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame into a thermal image
    heat_map, red_pixels = thermal_image(frame)

    # Display the thermal image
    cv2.imshow('Thermal Image', heat_map)

    # Print "Danger" if there are any red pixels
    if red_pixels > 0:
        cv2.putText(frame, st, (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        print("Danger")
    if red_pixels < 0:
        cv2.putText(frame, "Temps are safe for current climate", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        print("safe")

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

