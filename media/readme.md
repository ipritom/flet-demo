## Video Player
Currently flet has no in-built video player. We can read video frames with OpenCV. To update this in flet we have to run the OpenCV video source `read()` function in a seperate thread. 

To play your video, put your video path in the following line:
```python
cap = cv2.VideoCapture('video.mp4')

```