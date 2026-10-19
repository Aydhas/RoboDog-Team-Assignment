import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read from camera")
        break

    # Get frame dimensions (Height: 1080, Width: 1920)
    height, width, _ = frame.shape

    # Calculate zone boundaries
    third_1 = width // 3       # 640
    third_2 = (width * 2) // 3 # 1280

    # Convert the camera frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Lower and upper HSV limits for yellow
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Create a mask using cv2.inRange(...)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Find contours from the mask variable
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    command = "Searching..."
    
    if len(contours) > 0:
        # Select the largest contour by area
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        # Ignore tiny specks of noise (area < 500 pixels)
        if area > 500:
            # Calculate its bounding rectangle
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Draw the rectangle (Green) and centre point (Red) on the frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            center_x = x + w // 2
            center_y = y + h // 2
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            # --- STEP 3: STOP Condition (Area Ratio) ---
            frame_area = width * height
            area_ratio = (w * h) / frame_area
            
            # If the ball takes up more than 15% of the frame, it's too close
            if area_ratio > 0.15:
                command = "STOP"
            else:
                # --- STEP 1 & 2: Direction Zones ---
                if center_x < third_1:
                    command = "Turn Left"
                elif center_x <= third_2:
                    command = "Go Straight"
                else:
                    command = "Turn Right"

    # Draw the vertical boundaries on screen for visual reference
    cv2.line(frame, (third_1, 0), (third_1, height), (255, 0, 0), 2)
    cv2.line(frame, (third_2, 0), (third_2, height), (255, 0, 0), 2)

    # Display the command text on the frame
    cv2.putText(frame, f"Command: {command}", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)

    # Display the updated frame and mask
    cv2.imshow("Tracking Frame", frame)
    cv2.imshow("Yellow Mask", mask)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
