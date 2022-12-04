import flet as ft
import threading
import time

import cv2
import base64

cap = cv2.VideoCapture('video.mp4')

def main(page : ft.Page):
    page.title = "Video Player"

    def update_images():
        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                # encode the resulting frame
                jpg_img = cv2.imencode('.jpg', frame)
                b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
                image_box.src_base64 = b64_string
                page.update()
            else:
                break
            time.sleep(1/115)
        
         # when video is finished
        video_container.content.clean()
        video_container.content = ft.Text("Video Ended", size=20)
        page.update()
     
    b64_string = None         
    image_box = ft.Image(src_base64=b64_string, width=500, height=500)
    video_container = ft.Container(image_box, alignment=ft.alignment.center, expand=True)
    page.add(ft.Row([
        video_container
    ]
        
       
    ))

    ## theading 
    update_image_thread = threading.Thread(target=update_images)
    update_image_thread.daemon = True
    update_image_thread.start()

    page.update()

ft.app(target=main)