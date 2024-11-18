<h2> How to Set Up the Service </h2>
  
  **Installation Requirements:**
  
    Python 3.x
    
    zeromq library (pyzmq)
    
    Pillow library for image processing
    
    matplotlib for image display (client-side)


  **Directory set-up**

    /images
    /<topic1>
      image1.jpg
      image2.png
    /<topic2>
      image1.jpg
    server.py
    client.py

**Starting the Server:**
    
    Run the server script to start the microservice:
    
    photo_service_album.py
    
    The server will bind to tcp://*:5555 and wait for incoming requests.



<h2> Communication Contract </h2>

  Protocol
  
    The service communicates using the ZeroMQ REQ/REP pattern.
    
    Requests must be sent as strings, and responses are sent as JSON.
    
    Request Format

  To request image paths for a specific topic, the client must:

    Connect to the server at tcp://localhost:5555.
    
    Send a string message with the desired topic.

  Example Request
  
      socket.send_string("dogs")


Response Format

  The server responds with a JSON object containing the image paths:
  
  If images are found, the JSON object will contain a key images with a list of file paths.
  
  If no images are found, the images key will be an empty list.

  Example Response

    { "images": [ "./images/sunset/image1.jpg", "./images/sunset/image2.png" ] }


![Blank diagram - Page 1](https://github.com/user-attachments/assets/ae8b104d-bbb2-4599-be7c-73442323afa3)
