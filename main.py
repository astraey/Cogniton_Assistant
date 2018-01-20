from camera import Camera
from faceAPI import FaceAPI

camera = Camera()
image = camera.takePicture(True)

faceAPI = FaceAPI()

faceAPI.sendPicture(image)
