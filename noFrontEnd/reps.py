import cv2
import mediapipe as mp
import numpy as np
from yfunctions import *

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def repsfun(inp_leftangle, inp_rightangle, inp_lowleftangle, inp_lowrightangle):
    cap = cv2.VideoCapture(0)
    counter_left = 0
    counter_right = 0
    stage_left = None
    stage_right = None

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow_left = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist_left = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                angle_left = calculate_angle(shoulder_left, elbow_left, wrist_left)
                angle_right = calculate_angle(shoulder_right, elbow_right, wrist_right)

                if angle_left > inp_leftangle:
                    stage_left = "down"
                if angle_left < inp_lowleftangle and stage_left == 'down':
                    stage_left = "up"
                    counter_left += 1

                if angle_right > inp_rightangle:
                    stage_right = "down"
                if angle_right < inp_lowrightangle and stage_right == 'down':
                    stage_right = "up"
                    counter_right += 1

            except:
                pass

            cv2.imshow('Mediapipe Feed', image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    return counter_left, counter_right
