import cv2 as cv
import face_recognition
import csv
import os
import numpy as np
from datetime import datetime

video_capture = cv.VideoCapture(0)
path = "./students/"
students = os.listdir(path)
student_encode_list=[]

for student in students:
    student_img = face_recognition.load_image_file('./students/'+student)
    student_encode = face_recognition.face_encodings(student_img)[0]
    student_encode_list.append(student_encode)

know_student_names = [
     'Narendra Modi',
     'Allu Arjun',
     'Mohan lal ',
 ]
names_copy = know_student_names.copy()
#  Face from Camera
face_locations =[]
face_encodings =[]
face_names =[]
s= True

# Date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# csv file
headers =['ID', 'Student Name','Time came']
f = open(current_date+'.csv','w+',newline='')

lnwriter =csv.writer(f)
lnwriter.writerow(headers)
while True:
    _,video_data = video_capture.read()
    small_frame = cv.resize(video_data,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame =small_frame[:,:,:]

    if s:
        face_locations =face_recognition.face_locations(rgb_small_frame)
        face_encodings =face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names =[]

        for face_encoding in face_encodings:
            matches =face_recognition.compare_faces(student_encode_list,face_encoding)
            name=''
            face_distance =face_recognition.face_distance(student_encode_list,face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name =know_student_names[best_match_index]

            face_names.append(name)
            if name in know_student_names:
                if name in names_copy:
                    names_copy.remove(name)
                    print(names_copy)
                    current_time =now.strftime('%H:%M:%S')
                    lnwriter.writerow([best_match_index,name, current_time])
                
    cv.imshow("Attendance Management ",video_data)
    if cv.waitKey(1)==ord('q'):
        break
video_capture.release()
cv.destroyAllWindows()
f.close()