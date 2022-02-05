# Face Recognition

This project was developed using the python Face Recognition library which uses convolutional neural networks to identify face and verify their identity from an existing database of users.
<br />
How this works:
* Runs the video/image input through a convolutional neural network to identify the face
* Compares the face in the image with the faces in the dataset to find a match
* If a match isn't found, the image gets labelled as an intruder and an email gets sent to the admin with the image of the intruder attached
* If a match is found, the entry is logged into a MySQL database
<br /><br />
