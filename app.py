import cv2
import mediapipe as mp
from controller import Controller

# Create an instance of the Controller class
controller = Controller()

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.7
)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    if not success:
        break
    # The default in cv2 is BGR but hands instance only takes RGB-formatted video
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            controller.hand_Landmarks = landmarks  # Use the instance instead of class
            mpDraw.draw_landmarks(img, controller.hand_Landmarks, mpHands.HAND_CONNECTIONS)

            controller.update_fingers_status()  # Call on the instance
            controller.cursor_moving()
            controller.detect_scrolling()
            controller.detect_zoomming()
            controller.detect_clicking()
            controller.detect_dragging()

    cv2.imshow('Hand Tracker', img)  # Only one window for webcam feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()