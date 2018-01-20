import cv2

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def takePicture(self,savePictrure=False):
        print("This is a message inside the class.")

        self.camera = cv2.VideoCapture(0)
        return_value, image = self.camera.read()
        if savePictrure:
            cv2.imwrite('image.jpg', image)
            #print(image)
        return return_value   

    def closeCamera(self):
        del(self.camera)