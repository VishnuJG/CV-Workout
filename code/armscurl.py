import cv2
import mediapipe as mp
import numpy as np
import time
from mediapipe.framework.formats import landmark_pb2
# used for vizualizing the markings for pose detection
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose  # Pose estimation model
mp_drawing_styles = mp.solutions.drawing_styles

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)

# Video Feed
cap = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        res = pose.process(image)  # Making detections
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        blackie = np.zeros(image.shape)
        # print(res)
        x=list(mp_pose.POSE_CONNECTIONS)
        
        x=[e for e in x if e not in [(15,19), (15,17), (15,21), (16,22), (16, 18), (18,20), (16,20)]]
        for i in range(len(x)):
            w=list(x[i])
            if w[0]>=23:
                w[0]-=6
            if w[1]>=23:
                w[1]-=6
            x[i]=tuple(w)
        landmark_subset=res.pose_landmarks
        try :
            landmark_subset = landmark_pb2.NormalizedLandmarkList(landmark = [res.pose_landmarks.landmark[0],res.pose_landmarks.landmark[1],res.pose_landmarks.landmark[2],res.pose_landmarks.landmark[3],res.pose_landmarks.landmark[4], res.pose_landmarks.landmark[5], res.pose_landmarks.landmark[6], res.pose_landmarks.landmark[7], res.pose_landmarks.landmark[8], res.pose_landmarks.landmark[9], res.pose_landmarks.landmark[10], res.pose_landmarks.landmark[11], res.pose_landmarks.landmark[12], res.pose_landmarks.landmark[13], res.pose_landmarks.landmark[14], res.pose_landmarks.landmark[15], res.pose_landmarks.landmark[16], res.pose_landmarks.landmark[23], res.pose_landmarks.landmark[24], res.pose_landmarks.landmark[25], res.pose_landmarks.landmark[26], res.pose_landmarks.landmark[27], res.pose_landmarks.landmark[28], res.pose_landmarks.landmark[29], res.pose_landmarks.landmark[30], res.pose_landmarks.landmark[31], res.pose_landmarks.landmark[32]])
        except:
            pass
        # print(landmark_subset)
        # mp_drawing.draw_landmarks(blackie, res.pose_landmarks, mp_pose.POSE_CONNECTIONS, landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        mp_drawing.draw_landmarks(blackie, landmark_subset, x, landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        # try:
        #     mp_drawing.draw_landmarks(blackie, landmark_subset, mp_pose.POSE_CONNECTIONS)
        # except:
        #     mp_drawing.draw_landmarks(blackie, res.pose_landmarks, mp_pose.POSE_CONNECTIONS, landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        # print(res.pose_landmarks)
        # print("hi")

        # img = frame
        # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    #print(id,lm)
                    h, w, c = image.shape
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    #if id ==0:
                    cv2.circle(image, (cx,cy), 3, (255,0,255), cv2.FILLED)
                mp_drawing.draw_landmarks(blackie, handLms, mpHands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())

      

        # print(image)
        cv2.imshow("Mediapipe feed", cv2.flip(blackie, 1))

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
