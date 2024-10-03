
from collections import Counter
import time
import cv2
import pickle
import json
video = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


recognise = cv2.face.LBPHFaceRecognizer_create()
recognise.read("trainner.yml")
output = open('result_scan.txt','w')

labels = {} 
with open("labels.pickle", 'rb') as f:##
    og_label = pickle.load(f)##
    labels = {v:k for k,v in og_label.items()}##
    print(labels)
    t=3
names=""
while t:
    check,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
    count = 0
    last =""
    for x,y,w,h in face:
        face_save = gray[y:y+h, x:x+w]
        
      
        ID, conf = recognise.predict(face_save)
       
        if conf >= 40 and conf <= 115:
            if count > 30:
                
                transfer = {"name":ID}
                print(json.dumps(transfer))
                count = 0
            print(ID)
            if last == ID:
                count = count + 1
            print(labels[ID])
            output.write(labels[ID]+'\n')           
            cv2.putText(frame,labels[ID],(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX ,1, (18,5,255), 2, cv2.LINE_AA )
            last = ID
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,255),4)
        names= names+ " " +labels[ID]
    
    mins, secs = divmod(t, 60) 
    timer = '{:02d}:{:02d}'.format(mins, secs) 
    print(timer, end="\r") 
    time.sleep(1) 
    t -= 1
        
    cv2.imshow("Video",frame)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break
#make it a counter to then use the function to find the most common name in the list aka most frequently detected name
ctr= Counter(names.split()).most_common(1)
print("hi, ", ctr[0][0])
#end program
video.release()
cv2.destroyAllWindows()
