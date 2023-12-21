import cv2
from imutils.video import VideoStream
import time
import extMediaPipe as extMP
import fileManager as fm
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", default="output",
	help="path to output file for data collected")
args = vars(ap.parse_args())

# Get tooling for media pipe face mesh
(mp_drawing, mp_drawing_styles, mp_face_mesh) = extMP.get_drawing_tools()

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

with mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    while True:
        # Flip the image horizontally for a selfie-view display.
        frame = vs.read()
        frame = cv2.flip(frame, 1)

        # Swap BGR to RGB colours and process iamge
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        # Draw the face mesh annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                # Draws tesselation face mesh
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                
                # Draws media pipe landmarks (Eyes, Eye Bros, Lips, Face Oval)
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=extMP
                    .get_face_landmark_style())
                
                # Draws nose landmark
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=extMP.FACEMESH_FACE_NOSE,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=extMP
                    .get_face_landmark_style())

        # Add text to instruct user how to close program
        text = "Press \"ESC\" key to close program"
        cv2.putText(image, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display video and set video loop break
        cv2.imshow('MediaPipe Face Mesh', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break
    
# Clean up video and open cv
cv2.destroyAllWindows()
vs.stop()

## Save the Results
fm.save(args["output"], results, frame)
