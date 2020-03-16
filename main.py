import keras_ocr
import camera as cam
import helpers

if __name__ == "__main__": 
    # Prepare recognizer
    recognizer = keras_ocr.recognition.Recognizer()

    # Get image from the camera
    camera = cam.camera()

    # Ignore the first frame, which is typically blank on my machine
    image = camera.capture_frame(True) 

    # Perform recognition
    label = recognizer.recognize(image)

    # Perform TTS (speak label)
    helpers.sayText('The recognition result is: ' + label)
