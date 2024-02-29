import cv2 as cv # importing the opencv library
#a classifier is an algorithm that detects and give the positive if a face exists or not
# two main classifier that detect today are haar and local binary patterns

Hema=cv.imread("hema.jpg") #read the image of hemant gami

resize_image_Hema=cv.resize(Hema,(1000,1000)) # resize to a visible scale
cv.imshow("hema",resize_image_Hema) 

gray_scale=cv.cvtColor(resize_image_Hema,cv.COLOR_BGR2GRAY) # split it into grayscale
cv.imshow("hema_gray",gray_scale)

haar_Cascade=cv.CascadeClassifier("haar_face.xml") # reading the xml into haar cascade variable

faces_rect=haar_Cascade.detectMultiScale(gray_scale,scaleFactor=1.1,minNeighbors=3)
print(f'Number of face in the image is/are {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(resize_image_Hema,(x,y),(x+w,y+h),(0,25,255),thickness=2)

cv.imshow('Detected the Face',resize_image_Hema)

cv.waitKey(0)