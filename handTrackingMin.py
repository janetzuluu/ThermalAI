import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)
#create object for the hand using the hand detection module
mpHands=mp.solutions.hands
#only uses rgb elements
hands=mpHands.Hands()
mpdraw=mp.solutions.drawing_utils
#previous time
Ptime=0
#current time
Ctime=0

while True:
    success, img=cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #imgRGB=cv2.cvtcolor(img,cv2.color_BGR2RGB)
    results=hands.process(imgRGB)
    #will return the coordinates of he hands
    print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        #extract information for each hand.
        for handLms in results.multi_hand_landmarks:
            #we can track the coordinates, id and x and y coordinates
       # There are 21 hand landmarks, each composed of x, y and z coordinates. The x and y coordinates are normalized
       # to [0.0, 1.0] by the image width and height, respectively. The z coordinate represents the landmark depth,
       # with the depth at the wrist being the origin.
            for id,lm in enumerate(handLms.landmark):
                print(id,lm)
            #if hands are detected, this will draw dots on certain points of the img #hand connections will draw lines
            mpdraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
        #finds current time
        Ctime=time.time()
        #frame per second: time different pictures come tofether to form a video or picture
        fps=1/(Ctime-Ptime)
        #previous time will become the current ime
        Ptime=Ctime
        #IMG, dislay fps but first convert to string, position on screen, font, , color,
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


