import numpy as np
import cv2

def save(outputName, results, image):
    # Save the Data
    dataFileName = __checkExtension__(outputName, ".csv")
    __saveData__(dataFileName, results)

    # Save the image
    imageFileName = __checkExtension__(outputName, ".jpg")
    __saveImage__(imageFileName, image)

    print('Successfully saved')

# turns the lardmarks into a numpy array and stores it as a csv
def __saveData__(fileName, results):
    # Create array to store XYZ data for landmarks
    landmarks = results.multi_face_landmarks[0].landmark
    data = np.empty((3, len(landmarks)))

    # Store the XYZ data for each landmark
    for i in range(len(landmarks)):
        data[:, i] = (landmarks[i].x, landmarks[i].y, landmarks[i].z)   

    # Save to file
    np.savetxt(fileName, data, delimiter=",")

# uses open cv to store the image file
def __saveImage__(fileName, image):
        cv2.imwrite(fileName, image)

# checks if file is ending with proper extension
# or add the extension
def __checkExtension__(str, ext):
    if not str.endswith(ext):
        return str + ext
    return str