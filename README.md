# Face Mesh App

Welcome to my Face Mesh App – a solution for capturing intricate facial details and landmarks with precision. This application utilizes [Google's MediaPipe](https://developers.google.com/mediapipe), recognized as state-of-the-art technology. The app employs face mesh tessellation, pinpointing key facial features like eyes, chin, mouth, and nose, crucial for accurate face identification. Having explored alternatives such as [dlib](http://dlib.net/) and [Haar cascade](https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html), MediaPipe emerged as the optimal choice, excelling in versatility across diverse face types and lighting conditions while operating seamlessly in real-time. Notably, its efficiency with minimal system resources and compatibility with mobile edge devices positions it for future opportunities. The app, executed with a single command line, offers real-time visualization of the face mesh and landmarks. Upon completion, it captures a snapshot of the final face position and records mesh coordinates in a .csv file. While the current focus is on face mesh, the captured image, when coupled with a classification model, enables skin condition evaluation. Furthermore, the face mesh can be leveraged for Augmented Reality applications, facilitating tasks like makeup application or exploring various medical benefits. Dive into the forefront of facial analysis technology with the Face Mesh App, combining precision, efficiency, and future potential in a seamless package.

https://github.com/FareedQ/BlueSense/assets/5035155/5bb2588a-24df-4b20-9764-f59c3f6cb30e

**Note:** This video only shows the Face Mesh tessellation because it is more plesant to see. The application also highlights landmarks such as the eyes, nose, and face oval or chin.

## How to run the application

After installing all the dependancies, you can run the command `python3 main.py` to begin the application.

The ESC button will stop the application and save the results.

There is the option to `-output <filename>` to give the name of the output files. If nothing is given, it will use the word **output** for the files name.

## Requirements
There is a requirement file that will help install all the dependancies. Below are the main dependancies that required and installing them will install all the subdepenacies.
* [Python 3.9.6](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [imutils](https://pyimagesearch.com/2015/02/02/just-open-sourced-personal-imutils-package-series-opencv-convenience-functions/)
* [MediaPipe](https://developers.google.com/mediapipe)

## Next Steps

This application doesn't analyze any skin conditions and issues, that seems like a logical next step. It would be helpful if this app did split up the image to regions of interest as in [this tutorial](https://pyimagesearch.com/2017/04/10/detect-eyes-nose-lips-jaw-dlib-opencv-python/) which would be a good first step for preprocessing the image. I did not find pretrained skin categorization model so I belive I would have to architect and train one as a next step. I did find a [Dataset on Kaggle](https://www.kaggle.com/datasets/haroonalam16/20-skin-diseases-dataset/data) and an architecture for a [CCN on Kaggle](https://www.kaggle.com/code/chaitanya102000/skin-diseases-cnn). The MediaPipe framework also has this [Model Maker](https://developers.google.com/mediapipe/solutions/model_maker) which can help build a classification solution. I also came across a number of papers on this topic such as ([paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8074091/) and [paper](https://link.springer.com/chapter/10.1007/978-981-19-8032-9_39)) which can be used as inspiration for a developing a classification CNN.

## Additional Notes

* The MediaPipe landmarks did not include a nose landmark, so I had to create my own using this [diagram](https://i.stack.imgur.com/wDgvV.png). Click on the image to zoom-in.
* **imultils** is being used for the videostream. It is primarly used as a wrapper to ensure the threading of the is started and stopped properly. [Details here](https://github.com/PyImageSearch/imutils/blob/master/imutils/video/videostream.py)
* There is a **Warning Message** that may appear in the logs depending on the device you are running the application on. This is because of the MediaPipe library [here](https://github.com/google/mediapipe/blob/master/mediapipe/gpu/gl_context.cc#L357C14-L359).
* Another **Warning Message** appears to be created by the MediaPipe library [here](https://github.com/google/mediapipe/issues/4188) which is based on the access to the camera.

## References
A few tutorials I found very helpful on ramping up:
  * https://mediapipe.readthedocs.io/en/latest/solutions/face_mesh.html
  * https://www.assemblyai.com/blog/mediapipe-for-dummies/

## Bonus

After running the application and the data is saved, you can then run a second application which will process the data into a 3D visual layout. I came across this tutorial when researching the MediaPipe and thought it was fun. It could be useful to demonstrate and analyze 3d layouts of AR filters. To use this application, run the command `python3 plotData.py -data <yourCsvDataFile>` with a reference to the CSV file that was created. It will take a few seconds before completeing and generating a mp4 file like the one below.

https://github.com/FareedQ/BlueSense/assets/5035155/b41132ec-3ca5-46fc-87b9-6038325b82fa

