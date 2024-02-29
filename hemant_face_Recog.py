# import cv2 as cv
# import os 
# import numpy as np

# people=["Hemant Gami","Everyone Else"]
# P=[]
# # for i in os.listdir(r'C:\Users\Tanmay Somani\OneDrive\Desktop\opencv learning\Training_Images'):
# #     P.append(i)
# #     #P
# DIR=r'C:\Users\Tanmay Somani\OneDrive\Desktop\opencv learning\Training_Images'
# haar_Cascade=cv.CascadeClassifier("haar_face.xml") # reading the xml into haar cascade variable
# features=[]
# labels=[]

# def training():
#     for person in people:
#         path=os.path.join(DIR,person)
#         label=people.index(person)

#         for img in os.listdir(path):
#             img_path=os.path.join(path,img)

#             img_array=cv.imread(img_path)
#             gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

#             faces_rect=haar_Cascade.detectMultiScale(gray,1.1,4)

#             for(x,y,w,h) in faces_rect:
#                 faces_ROI=gray[y:y+h,x:x+w]
#                 features.append(faces_ROI)
#                 labels.append(label)

# training()

# # print(f'Length of the features list is equal to {len(features)}')
# # print(f'Length of the labels list is equal to {len(labels)}')
# features=np.array(features,dtype="object")
# labels=np.array(labels)

# face_recog=cv.face.LBPHFaceRecognizer.create()
# #Train the recognizer on the features and the labels list

# face_recog.train(features, labels)

# np.save("features.npy",features)
# np.save("labels.npy",labels)


# cv.waitKey(0)

import os
import cv2 as cv
import numpy as np

people=["Hemant gami","Everyone Else"]
DIR=r'C:\Users\Tanmay Somani\OneDrive\Desktop\opencv learning\Training_Images'

haar_cascade=cv.CascadeClassifier("haar_face.xml")
features=[]
labels=[]

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            resize_img=cv.resize(img_array,(720,720))
            cv.imshow(f"{img}",resize_img)
            gray=cv.cvtColor(resize_img,cv.COLOR_BGR2GRAY)

            faces_rect=haar_cascade.detectMultiScale(gray,1.1,4,3,(3,3))  
            
            for(x,w,y,h) in faces_rect:
                faces_roi=gray[y:y+h,w:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Training completed __________")
print(f'The number of features are {len(features)}')
print(f'The number of labels are {len(labels)}')
features=np.array(features,dtype="object")
labels=np.array(labels)
face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
