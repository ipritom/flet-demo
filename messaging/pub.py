import time
from Znode import Node


publisher = Node(node_type="PUB")

while True:
    publisher.publish("update", f"{time.time()}")
    

