import cv2
import mediapipe as mp
import numpy as np
from mediapipe.framework.formats import landmark_pb2
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        res = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        blackie = np.zeros(image.shape)
        x = list(mp_pose.POSE_CONNECTIONS)
        x = [e for e in x if e not in [(15,19), (15,17), (15,21), (16,22), (16, 18), (18,20), (16,20)]]
        landmark_subset = res.pose_landmarks
        try:
            landmark_subset = landmark_pb2.NormalizedLandmarkList(landmark=[res.pose_landmarks.landmark[i] for i in range(33)])
        except:
            pass
        mp_drawing.draw_landmarks(blackie, landmark_subset, x)
        results = hands.process(image)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(image, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
                mp_drawing.draw_landmarks(blackie, handLms, mpHands.HAND_CONNECTIONS)
        cv2.imshow("Mediapipe feed", cv2.flip(blackie, 1))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
