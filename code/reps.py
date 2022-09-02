import cv2
import mediapipe as mp
import numpy as np
from yfunctions import *

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


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
            
            
            shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow_left = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist_left = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            
            angle_left = calculate_angle(shoulder_left, elbow_left, wrist_left)
            angle_right = calculate_angle(shoulder_right, elbow_right, wrist_right)
            
            
            cv2.putText(image, str(angle_left), 
                           tuple(np.multiply(elbow_left, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 150), 2, cv2.LINE_AA
                                )
            cv2.putText(image, str(angle_right), 
                           tuple(np.multiply(elbow_right, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 150), 2, cv2.LINE_AA
                                )
            
            
            if angle_left > 160:
                stage_left = "down"
            if angle_left < 30 and stage_left =='down':
                stage_left="up"
                counter_left +=1
                print("left : "+str(counter_left))

            if angle_right > 160:
                stage_right = "down"
            if angle_right < 30 and stage_right =='down':
                stage_right = "up"
                counter_right +=1
                print("right : "+str(counter_right))
                       
        except:
            pass
        
        
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )   
        image=cv2.flip(image, 1)
        
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        
        
        cv2.putText(image, 'REPS', (15,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter_left), 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)


        cv2.rectangle(image, (225+200,0), (450+200,73), (245,117,16), -1)
        
        cv2.putText(image, 'REPS', (240+200,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter_right), 
                    (235+200,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        
        
        cv2.putText(image, 'STAGE', (65,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, stage_left, 
                    (60,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)


        cv2.putText(image, 'STAGE', (65+425,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, stage_right, 
                    (60+425,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        
        
        

        blackie = np.zeros(image.shape)
        mp_drawing.draw_landmarks(blackie, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 ) 
        blackie=cv2.flip(blackie, 1)
        
        cv2.imshow('Mediapipe Feed', image)
        cv2.imshow('Blackie', blackie)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

