import cv2 as cv 
import numpy as np 

cap = cv.VideoCapture(0)
avg = 0
avgYellowCount = 0
avgRedCount = 0 
avgGreenCount = 0

deger = True
print("started")

while avg < 100:
    firstYellowCount = 0
    firstRedCount = 0
    firstGreenCount = 0
    ret,frame = cap.read()
    frame = cv.flip(frame,1)
    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    cv.imshow("Webcam",frame)
    
        
 #red detection
    #lower_red1 = np.array([0,100,20])
    #upper_red1 = np.array([10,255,255])
    lower_red2 = np.array([160,100,20])
    upper_red2 = np.array([179,255,255])
    #red_mask = cv.inRange(hsv_frame,lower_red1,upper_red1)
    red_mask2 = cv.inRange(hsv_frame,lower_red2,upper_red2)
    #full_red_mask = red_mask + red_mask2
    red = cv.bitwise_and(frame,frame,mask = red_mask2)
    for i in range(len(red)):
        if(np.sum(red[i]) != 0):
            firstRedCount += 1
    
    
 #yellow detection
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv.inRange(hsv_frame,lower_yellow,upper_yellow)
    yellow = cv.bitwise_and(frame,frame,mask = yellow_mask)
    for i in range(len(yellow)):
        if(np.sum(yellow[i]) != 0):
            firstYellowCount += 1
        

    
#green detection 
    lower_green = np.array([45,100,50])
    upper_green = np.array([75,255,255])
    green_mask = cv.inRange(hsv_frame,lower_green,upper_green)
    green = cv.bitwise_and(frame,frame,mask = green_mask)
    hGreen,sGreen,vGreen = cv.split(green)
    for i in range(len(green)):
        if(np.sum(green[i]) != 0):
            firstGreenCount += 1
        
    
    #print("R - Y - G : ",firstRedCount, " - ",firstYellowCount, " - ",firstGreenCount)
    avgGreenCount += firstGreenCount
    avgYellowCount += firstYellowCount
    avgRedCount += firstRedCount
    avg += 1    
            
avgGreenCount /= 1000    
avgRedCount /= 100
avgYellowCount /= 100

while deger:
    firstYellowCount = 0
    firstRedCount = 0
    firstGreenCount = 0
    ret,frame = cap.read()
    frame = cv.flip(frame,1)
    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    cv.imshow("Webcam",frame)
    
        
 #red detection
    #lower_red1 = np.array([0,100,20])
    #upper_red1 = np.array([10,255,255])
    lower_red2 = np.array([160,100,20])
    upper_red2 = np.array([179,255,255])
    #red_mask = cv.inRange(hsv_frame,lower_red1,upper_red1)
    red_mask2 = cv.inRange(hsv_frame,lower_red2,upper_red2)
    #full_red_mask = red_mask + red_mask2
    red = cv.bitwise_and(frame,frame,mask = red_mask2)
    for i in range(len(red)):
        if(np.sum(red[i]) != 0):
            firstRedCount += 1
    
    
 #yellow detection
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv.inRange(hsv_frame,lower_yellow,upper_yellow)
    yellow = cv.bitwise_and(frame,frame,mask = yellow_mask)
    for i in range(len(yellow)):
        if(np.sum(yellow[i]) != 0):
            firstYellowCount += 1
        

    
#green detection 
    lower_green = np.array([45,100,50])
    upper_green = np.array([75,255,255])
    green_mask = cv.inRange(hsv_frame,lower_green,upper_green)
    green = cv.bitwise_and(frame,frame,mask = green_mask)
    hGreen,sGreen,vGreen = cv.split(green)
    for i in range(len(green)):
        if(np.sum(green[i]) != 0):
            firstGreenCount += 1
        
    diffGreen = firstGreenCount - avgGreenCount
    diffYellow = firstYellowCount - avgYellowCount
    diffRed = firstRedCount - avgRedCount
    
    if(diffGreen > 50 and diffGreen > diffRed and diffGreen > diffYellow):
        print("Run!")
    if(diffYellow > 50 and diffYellow > diffRed  and diffYellow > diffGreen):
        print("Be Ready!")
    if(diffRed > 75 and diffRed > diffGreen and diffRed > diffYellow):
        print("Stop!")
    
    if cv.waitKey(1) & 0xFF == ord("q"):    
        deger = False
    
    

print("finished")
cap.release()
cv.destroyAllWindows()