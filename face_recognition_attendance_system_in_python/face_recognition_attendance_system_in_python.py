# required libraries for this project
#opne-cv
#cmake
#dlib
#face_recognition
#numpy
# and visual studio build tools==> download it from its website
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Video capture from default camera (0)
video_capture = cv2.VideoCapture(0)

# Load known images and their encodings
malki_image = face_recognition.load_image_file("known_faces/malki.png")
malki_encoding = face_recognition.face_encodings(malki_image)[0]

hasnat_image = face_recognition.load_image_file('known_faces/hasnat.jpeg')
hasnat_encoding = face_recognition.face_encodings(hasnat_image)[0]

junaid_image = face_recognition.load_image_file("known_faces/junaid.jpeg")
junaid_encoding = face_recognition.face_encodings(junaid_image)[0]

hamza_image = face_recognition.load_image_file('known_faces/hamza.jpg')
hamza_encoding = face_recognition.face_encodings(hamza_image)[0]

# List of known face encodings and corresponding names
known_face_encodings = [malki_encoding, hasnat_encoding, junaid_encoding, hamza_encoding]
known_face_names = ['Malki Aman', 'Hasnat Ali', 'Junaid Hussain', 'Hamza Alam']

# List of students initially
students = known_face_names.copy()

# Initialize variables for face detection
face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%d-%m-%y")

# Open CSV file to log attendance
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    # Capture a single frame of video
    _, frame = video_capture.read()
    
    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    # Recognize faces in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    for face_encoding in face_encodings:
        # Compare face encodings with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            
            # Display name on the video frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (0, 255, 0)  # green color
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText,
                        font, fontScale, fontColor, thickness, lineType)
            
            # Record attendance if the person is in the students list
            if name in students:
                students.remove(name)
                current_time = now.strftime("%I:%M:%S %p")
                lnwriter.writerow([name, current_time])
    
    # Display the video frame with attendance info
    cv2.imshow("Attendance", frame)
    
    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()

# Close the CSV file
f.close()
