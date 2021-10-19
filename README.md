# scan_rotation
![effect](https://user-images.githubusercontent.com/56223390/137892863-3af46488-bb93-4682-91e2-082e587edfcd.png)

#Process description

We often misplace the document in the scanning area of the printer. That is why this project was created.
Its aim was to train a neural network that would allow the rotation of scanned documents according to our reading direction.
I used the template from the tutorial to train the network:

The first problem I encountered was finding the set of scanned documents I needed to train the network.
Below I present the dataset that I found after a long search.

Data processing consisted of extracting them from jammed directories. Then it was necessary to convert them to * .jpeg format

I divided the files into four directories and then rotated them. Here I made one of the biggest mistakes.
I tried to rotate the files with the tool from the Windows context menu. This rotation added information to the image metadata about the need to rotate the image before opening it.
The activated neural network took files directly without making this rotation, so I lost quite a lot of time on unsuccessful attempts to train the network.

The result I was able to get is 99.x% for 4 possibilities of document rotation. 
