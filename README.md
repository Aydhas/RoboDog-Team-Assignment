# RoboDog-Team-Assignment
1. What I built
I created a computer vision program in python using OpenCV which detects a yellow ball in real time through a webcam. The program shows a live video feed and a binary mask with a green bounding box, a red center point, dynamic direction commands and a STOP alert overlayed.

2. How it works
The script grabs webcam frames in a loop, converts the BGR frames to HSV and then filters yellow pixels using the cv2.inRange() function. Then, it finds the contours from the mask, chooses the biggest valid region, and computes its center coordinates. It compares the center with three horizontal zones of the frame and orders to “Turn Left”, “Go Straight” or “Turn Right”. If the bounding box area ratio is larger than a safe limit, it will set “STOP”.

3. Challenges faced
One of the most difficult problems was the ambient lighting variations that changed the apparent shade of the ball and added background noise. I solved this by carefully tuning the HSV threshold bounds and filtering out small contours (<500 pixels). Furthermore, the implementation of the STOP condition involved a realisation that the bounding-box area ratio is merely a rough visual estimate of closeness, not a true physical distance measurement.

4. What I would do next
Then I would use adaptive colour tracking to automatically adjust for changes in light in the room. I would also add colour histogram filtering to prevent false positives on yellow objects in the background and explore stereo vision or depth estimation for more accurate stopping distances.
<img width="451" height="571" alt="image" src="https://github.com/user-attachments/assets/f13d90aa-627e-4fa5-913a-641b4f9da27f" />
