import flet as ft
from Znode import Node
import threading


client = Node(node_type="SUB")

def main(page:ft.Page):
    client.subscribe("update")

    # text update function (will be in thread)
    def update_thread():
        while True:
            pkt, success = client.receive()
            topic, msg = pkt

            if success:
                update_text.value = msg.decode()
                page.update()


    # Create a thread and pass the page object to update it
    thread = threading.Thread(target=update_thread, daemon=True)
    thread.start()

    # page ui config
    page.title = "Znode Demo"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    update_text = ft.Text("Hello, ready for receving messages?", size=30)

    # add ui element to page
    page.add(
        update_text
    )

ft.app(target=main)
