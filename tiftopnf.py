import os, sys
from PIL import Image

n = 0
for infile in os.listdir("./"):
    print("file : " + infile)
    if infile[-3:] == "tif":
       outfile = infile[:-3] + "jpeg"
       im = Image.open(infile)
       out = im.convert("RGB")
       out.save(outfile, "JPEG", quality=90)
print("end")
