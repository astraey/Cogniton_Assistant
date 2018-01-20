from camera import Camera
from faceAPI import FaceAPI

camera = Camera()
faceAPI = FaceAPI()

picTaken = camera.takePicture(True)

if picTaken:
	faceAPI.sendPicture(camera.picName)
