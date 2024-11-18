import zmq
import os
from PIL import Image
import io
import json

# Set up the connection for the zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
# Bind the port for communication
socket.bind("tcp://*:5555")
print("Service is running")


def get_images_from_topic(topic):
    # Get the image paths from the folders for the interests
    folder = f'./images/{topic}'
    if not os.path.exists(folder):
        return []

    # Get all image files in the folder
    image_files = [f for f in os.listdir(
        folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_paths = [os.path.join(folder, file) for file in image_files]
    return image_paths


def resize_image(image_path):
    """Resize image to fit within the canvas."""
    try:
        image = Image.open(image_path)
        image.thumbnail((300, 300))  #
        byte_arr = io.BytesIO()
        image.save(byte_arr, format='PNG')
        return byte_arr.getvalue()
    except Exception as e:
        print(f"Error resizing image {image_path}: {e}")
        return None


while True:
    # Wait for a request from the main program
    message = socket.recv_string()
    topic = message.strip()

    # Get the images for the topic
    images = get_images_from_topic(topic)

    # Send back the list of image paths in JSON
    socket.send_json({'images': images})
