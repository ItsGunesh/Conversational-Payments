import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Face Mesh
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=3)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

# Start the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    # print("Akshat")

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)

    img = cv2.resize(img, (640, 480))
    cv2.imshow("Webcam Feed", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()

