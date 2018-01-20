import cv2

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.picName = 'image.jpg'

    def takePicture(self, pictureName=None, savePictrure=False):
        if pictureName is not None:
            self.picName = pictureName 

        self.camera = cv2.VideoCapture(0)
        return_value, image = self.camera.read()
        if savePictrure:
            cv2.imwrite(self.picName, image)
        return return_value   

    def closeCamera(self):
        del(self.camera)