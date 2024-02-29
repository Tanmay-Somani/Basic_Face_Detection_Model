import numpy as np
import cv2 as cv
import os

haar_cascade=cv.CascadeClassifier('haar_face.xml')
i=0
features=np.load("features.npy",allow_pickle=True)
lables=np.load("labels.npy",allow_pickle=True)

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

DIR=r'C:\Users\Tanmay Somani\OneDrive\Desktop\opencv learning\Training_Images'

people=["Hemant gami","Everyone Else"]
for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            img=cv.resize(img_array,(720,720))
            gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            face_rect=haar_cascade.detectMultiScale(gray,1.1,4)

            for(x,y,w,h) in face_rect:
                faces_roi=gray[y:y+h,x:x+w]

                label,confidence=face_recognizer.predict(faces_roi)

                print(f'Label={people[label]} with a confidence of {confidence}')
                cv.putText(img,str(people[label]+" Confidence "+str(round(confidence,2))),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,255),thickness=2)
                cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0))
                
                if confidence<50:
                    cv.imshow(f'Face Detected {i}',img)
                else:
                    cv.imshow(f'Face Not Detected {i}',img)
                i+=1
                    





cv.waitKey(0)
