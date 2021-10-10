
import cv2
import mediapipe as mp
import time
import os
import numpy as np 
import face_recognition
from datetime import datetime
import pyodbc

face_cascade = cv2.CascadeClassifier('./src/face_dection.xml')

path= 'photo_db'
images=[]
imgLabel=[]
mylst=os.listdir(path)

for cl in mylst:
    curimg=cv2.imread(f'{path}\\{cl}')
    images.append(curimg)
    imgLabel.append(os.path.splitext(cl)[0])
    
#print(classNames)

def findEncodings(images):
    encodLst=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodLst.append(encode)
    return encodLst

encodlstKnowFaces=findEncodings(images)


#connicted with database.
conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=MSI;'
                    'Database=attendancedb;'
                    'Trusted_Connection=yes;')
cursor = conn.cursor()


def markAttendance(id_f,Name_f,Indate, Intime, Outdate, Outtime):

    sql='''insert into attendancedb.dbo.tbl_attendance (id_f,Name_f,Indate, Intime, Outdate, Outtime) values(?, ?,?,?, ?,?)'''

    val=(id_f,Name_f,Indate, Intime, Outdate, Outtime)
    cursor.execute(sql,val)
    conn.commit()
    

webcam=cv2.VideoCapture(0)
nm=""


while True:

    crTime=datetime.now()
    crDate=datetime.now()

    success, img=webcam.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    
    faceCurFrm= face_recognition.face_locations(imgS)
    encodeCurFrm=face_recognition.face_encodings(imgS,faceCurFrm)

    for encodFace, faseLocation in zip(encodeCurFrm,faceCurFrm):
        maches=face_recognition.compare_faces(encodlstKnowFaces,encodFace)
        faceDis=face_recognition.face_distance(encodlstKnowFaces,encodFace)
        
        machesIndex=np.argmin(faceDis)

        y1,x2,y2,x1=faseLocation
        y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4


        if maches[machesIndex]:
            name = imgLabel[machesIndex].upper()
            # print(name)

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3) 

            cv2.putText(img,name,(x1+6,y2+30),cv2.FONT_HERSHEY_COMPLEX ,1,(255,255,255),2) # text coloer wite 

            if name!=nm:
                markAttendance(name,'',str(crDate.date()),str(crTime.time()),'','')
                nm=name
        else: 
            Knname="Please try again"
            faces = face_cascade.detectMultiScale(imgS, 1.1, 2)
            for (x, y, w, h) in faces:
                # color "(0,0,255)" is blue but show Red (-120°): 
                # if you want you cant test color "https://www.the3rdsequence.com/"
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),3) 
                cv2.putText(img,Knname,(x1+6,y2+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        

    cv2.imshow('Webcam',img)
    if cv2.waitKey(20) & 0xFF == 27: # code 27 == 'ESC' KEY
        break

    cv2.waitKey(1)

webcam.release()
cv2.destroyAllWindows()














# class FaceDetector():
#     def __init__(self, minDetectionCon=0.5):
 
#         self.minDetectionCon = minDetectionCon
 
#         self.mpFaceDetection = mp.solutions.face_detection
#         self.mpDraw = mp.solutions.drawing_utils
#         self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)
 
#     def findFaces(self, img, draw=True):

#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.faceDetection.process(imgRGB)
#         # print(self.results)
#         bboxs = []
#         if self.results.detections:
#             for id, detection in enumerate(self.results.detections):
#                 bboxC = detection.location_data.relative_bounding_box
#                 ih, iw, ic = img.shape
#                 bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
#                        int(bboxC.width * iw), int(bboxC.height * ih)
#                 bboxs.append([id, bbox, detection.score])
#                 if draw:
#                     img = self.fancyDraw(img,bbox)
                    
#         return img, bboxs
 
#     def fancyDraw(self, img, bbox, l=30, t=5, rt= 1):
#         x, y, w, h = bbox
#         x1, y1 = x + w, y + h
 

#         #cv2.rectangle(img, bbox, (112, 25, 25), rt) #To set Box 
#         # Top Left  x,y
#         cv2.line(img, (x, y), (x + l, y), (112, 25, 25), t)
#         cv2.line(img, (x, y), (x, y+l), (112, 25, 25), t)
#         # Top Right  x1,y
#         cv2.line(img, (x1, y), (x1 - l, y), (112, 25, 25), t)
#         cv2.line(img, (x1, y), (x1, y+l), (112, 25, 25), t)
#         # Bottom Left  x,y1
#         cv2.line(img, (x, y1), (x + l, y1), (2112, 25, 25), t)
#         cv2.line(img, (x, y1), (x, y1 - l), (112, 25, 25), t)
#         # Bottom Right  x1,y1
#         cv2.line(img, (x1, y1), (x1 - l, y1), (112, 25, 25), t)
#         cv2.line(img, (x1, y1), (x1, y1 - l), (112, 25, 25), t)
#         return img
 


 
# def main():
#     cap = cv2.VideoCapture(0)
#     nm="a"

#     pTime = 0
#     detector = FaceDetector()
#     while True:
#         success, img = cap.read()
#         img, bboxs = detector.findFaces(img)
#         #print(bboxs)

        

#         success, img=cap.read()
#         imgS=cv2.resize(img,(0,0),None,0.25,0.25)
#         imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

#         faceCurFrm= face_recognition.face_locations(imgS)
#         encodeCurFrm=face_recognition.face_encodings(imgS,faceCurFrm)

#         for encodFace, faseLocation in zip(encodeCurFrm,faceCurFrm):
#             maches=face_recognition.compare_faces(encodlstKnowFaces,encodFace)
#             faceDis=face_recognition.face_distance(encodlstKnowFaces,encodFace)
            
#             machesIndex=np.argmin(faceDis)

#             if maches[machesIndex]:
#                 name = imgLabel[machesIndex].upper()
#                 # print(name)


#                 y1,x2,y2,x1=faseLocation


#                 y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
#                 cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
#                 cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#                 cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX ,1,(255,255,255),2)
                
#                 crTime=datetime.now().time()
#                 crDate=datetime.now().date()
#                 if name!=nm:

#                     markAttendance2(id,name,str(crTime),str(crDate),str(crTime),str(crDate))
#                     nm=name





 
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#         cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
#         cv2.imshow("Image", img)

#         if cv2.waitKey(20) & 0xFF == 27: # code 27 == 'ESC' KEY
#             break

#         cv2.waitKey(1)
 
 
# if __name__ == "__main__":
#     main()