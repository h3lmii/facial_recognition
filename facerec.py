import cv2
import face_recognition
import os
import numpy as np
import time
import tkinter as tk


def add():
    haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    capi = cv2.VideoCapture(0)
    top=tk.Tk()
    while True:
        successi, imgi = capi.read()
        gray_img = cv2.cvtColor(imgi, cv2.COLOR_BGR2GRAY)
        faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)
        for (x, y, w, h) in faces_rect:
            cv2.rectangle(imgi, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)


        cv2.imshow('Webcam',imgi)

        
        if cv2.waitKey(1) & 0xFF == ord('s'):
         
           
            
            name_label = tk.Label(top, text = 'NAME', font=('calibre',15, 'bold'))
            name_label.place(x=10,y=40)
            E1 = tk.Entry(top, width=25,font=('calibre',15))
            E1.place(x=80, y=40)

            def submit():
                x=E1.get()


                cv2.imwrite(r"photos/{}.jpg".format(x),imgi)
                print('Saved' ,x)
                top.destroy()
                capi.release()
                cv2.destroyAllWindows()
            b=tk.Button(top,text="ENTER",font=("Algerian",15),bg='green',fg='white',command=submit)
            b.place(x=380, y=35)
            top.geometry("500x100")

            top.mainloop()
                
            break


            #cv2.waitKey(1)
        
    capi.release()
    cv2.destroyAllWindows()
    
    
    

def detect_face() :

    haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    imgs=[]
    known_encodings = []

    known_names = []
    known_dir =os.getcwd()+'/photos'

    for file in os.listdir(known_dir):
        img = cv2.imread(known_dir + '/' + file)
        imgs.append(img)
        try:
                img_enc = face_recognition.face_encodings(img)[0]

        except IndexError as e:
            pass
        

        known_encodings.append(img_enc)
        known_names.append(file.split('.')[0])
    print(known_names)

    cap = cv2.VideoCapture(0)
     
    while True:
        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
         
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(known_encodings,encodeFace)
            faceDis = face_recognition.face_distance(known_encodings,encodeFace)
            print(faceDis)
            if  faceDis.min()<0.53:
                matchIndex = np.argmin(faceDis)
            else:
                matchIndex=-1
                matches[matchIndex]=False


            

            
            if matches[matchIndex]:
                name = known_names[matchIndex].upper()
                #print(name)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-30),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                
            
            else:
                gray_img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces_rect = haar_cascade.detectMultiScale(gray_img1, scaleFactor=1.1, minNeighbors=9)
                for (x, y, w, h) in faces_rect:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)
                    cv2.rectangle(img,(x,y-30),(x,y),(0,0,255),cv2.FILLED)
                    cv2.putText(img,'UNKOWN',(x+6,y-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)



    
                
         
        cv2.imshow('Webcam',img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('success.jpg',img)
            print('welcome' ,name)

            break
        


        #cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()

