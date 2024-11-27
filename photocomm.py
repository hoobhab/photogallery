import zmq
import os
from PIL import Image
import matplotlib.pyplot as plt
import math

# Set up zmq for communication
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Connect to the microservice


def display_images(image_paths):
    # Display images to the grid using matplotlib(?)
    if not image_paths:
        print("No images to display.")
        return

    # Determine the grid size by # of images
    num_images = len(image_paths)
    num_columns = 3  # length of images per column
    num_rows = math.ceil(num_images / num_columns)

    # Create a map to display images in a grid
    fig, axes = plt.subplots(num_rows, num_columns, figsize=(12, 12))
    axes = axes.flatten()

    for idx, image_path in enumerate(image_paths):
        if os.path.exists(image_path):
            image = Image.open(image_path)
            axes[idx].imshow(image)
            axes[idx].axis('off')
        else:
            print(f"Image not found: {image_path}")
            axes[idx].axis('off')

    for j in range(num_images, len(axes)):
        axes[j].axis('off')

    # Adjust the layout and display the images to the user
    plt.subplots_adjust(wspace=0.7, hspace=0.8)
    manager = plt.get_current_fig_manager()
    manager.resize(800, 700)
    plt.tight_layout()
    plt.show()


def request_images(topic):
    # Send the topic to the microservice
    socket.send_string(topic)

    # Wait for the response from the server
    response = socket.recv_json()

    if 'images' in response and response['images']:
        display_images(response['images'])
    else:
        print(f"No images found for the topic: {topic}")


if __name__ == "__main__":
    request_images()
