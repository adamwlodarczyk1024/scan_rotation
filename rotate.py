from PIL import Image

# import os utilities
import os

# define a function that rotates images in the current directory
# given the rotation in degrees as a parameter
n = 0
def rotateImages(rotationAmt):
  # for each image in the current directory
  for image in os.listdir(os.getcwd()):
    # open the image
    img = Image.open(image)
    # rotate and save the image with the same filename
    img.rotate(rotationAmt).save(image)
    # close the image
    img.close()
    n =+ 1
    print(n)
# examples of use
rotateImages(270)
