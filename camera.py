import cv2 as opencv

class camera(object):
    def __init__(self):
        # Initialize the camera capture
        self.camera_capture = opencv.VideoCapture(0)
        
    def capture_frame(self, ignore_first_frame):
        # Get frame, ignore the first one if needed
        if(ignore_first_frame):
            self.camera_capture.read()
            
        (capture_status, self.current_camera_frame) = self.camera_capture.read()

        # Verify capture status
        if(capture_status):
            return self.current_camera_frame

        else:
            # Print error to the console
            print('Capture error')
