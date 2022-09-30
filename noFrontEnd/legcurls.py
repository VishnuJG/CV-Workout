import cv2
import mediapipe as mp
import numpy as np
from yfunctions import *


def legscurlfun(inp_leftangle, inp_rightangle, inp_lowleftangle, inp_lowrightangle):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose


    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(0)

    left_color=(255,0,0)
    right_color=(255,0,0)
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
            blackie = np.zeros(image.shape)


            try:
                landmarks = results.pose_landmarks.landmark

                ankle_left = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                knee_left = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                hip_left = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                ankle_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                knee_right = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                hip_right = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                
                angle_left = calculate_angle(ankle_left, knee_left, hip_left)
                angle_right = calculate_angle(ankle_right, knee_right, hip_right)
                
                image = cv2.flip(image, 1)
                
                
                cv2.putText(blackie, str(angle_left),
                            tuple(np.multiply(knee_left, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,
                                                            0, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(blackie, str(angle_right),
                            tuple(np.multiply(knee_right, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,
                                                            0, 255), 2, cv2.LINE_AA
                            )
                image = cv2.flip(image, 1)
                if angle_left > inp_leftangle:
                    stage_left = "up"
                    
                if angle_left < inp_lowleftangle and stage_left == 'up':
                    stage_left = "down"
                    counter_left += 1
                    
                    print("left : "+str(counter_left))

                if angle_right > inp_rightangle:
                    stage_right = "up"
                    
                if angle_right < inp_lowrightangle and stage_right == 'up':
                    stage_right = "down"
                    counter_right += 1
                    
                    print("right : "+str(counter_right))


                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(
                                        color=(245, 117, 66), thickness=2, circle_radius=2),
                                    mp_drawing.DrawingSpec(
                                        color=(245, 66, 230), thickness=2, circle_radius=2)
                                    )
                image = cv2.flip(image, 1)


                if angle_left<=inp_leftangle and angle_left>=inp_lowleftangle:
                    left_color=(0,255,0)
                else:
                    left_color=(0,0,255)
                if angle_right<=inp_rightangle and angle_right>=inp_lowrightangle:
                    right_color=(0,255,0)
                else:
                    right_color=(0,0,255)

                cv2.rectangle(image, (0, 0), (225, 73), left_color, -1)

                cv2.putText(image, 'REPS', (15, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(counter_left),
                            (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)

                cv2.rectangle(image, (225+200, 0), (450+200, 73), right_color, -1)

                cv2.putText(image, 'REPS', (240+200, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(counter_right),
                            (235+200, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)

                cv2.putText(image, 'STAGE', (65, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, stage_left,
                            (60, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)

                cv2.putText(image, 'STAGE', (65+425, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, stage_right,
                            (60+425, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)


                cv2.putText(image, str(round(angle_left)), 
                            (10,100), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, left_color, 2, cv2.LINE_AA)
                cv2.putText(image, str(round(angle_right)), 
                            (235+200,100), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, right_color, 2, cv2.LINE_AA)

            except:
                image = cv2.flip(image, 1)
                pass

            
                        
            
            mp_drawing.draw_landmarks(blackie, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(
                                        color=(245, 117, 66), thickness=2, circle_radius=2),
                                    mp_drawing.DrawingSpec(
                                        color=(245, 66, 230), thickness=2, circle_radius=2)
                                    )
            blackie = cv2.flip(blackie, 1)

            cv2.imshow('Mediapipe Feed', image)
            cv2.imshow('Blackie', blackie)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    return [counter_right, counter_left]
