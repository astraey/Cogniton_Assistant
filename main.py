from camera import Camera
from faceAPI import FaceAPI
from beeper import Beeper
import time

camera = Camera()
faceAPI = FaceAPI()
beeper = Beeper()
endTime = time.time() + 60*10

while time.time() < endTime:


    picTaken = camera.takePicture(savePictrure=True)

    if picTaken:
        temp = faceAPI.sendPicture(camera.picName)
    if temp:
        beeper.makeSound(temp[0]['faceAttributes']['emotion'])
    else:
        print("No Faces were detected")
    camera.closeCamera()
    time.sleep(0.1)

beeper.close()
