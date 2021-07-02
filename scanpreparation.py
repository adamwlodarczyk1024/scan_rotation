# Place where i make pdf transform
# i use this dataset https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DJHVHB
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

# place where you have pdf multiscan
path = "C:\\Users\\Adam\\Documents\\dane do ml\\pdf"
COUNT = 1

def renamefiles(text):
    os.chdir(path)
    # Function to increment count
    # to make the files sorted.
    def increment():
        global COUNT
        COUNT = COUNT + 1

    for f in os.listdir(path):
        f_name, f_ext = os.path.splitext(f)
        f_name = text + str(COUNT)
        increment()

        new_name = '{}_zmiana{}'.format(f_name, f_ext)
        os.rename(f, new_name)



def splitpdf():
    os.chdir(path)
    for filename in os.listdir(path):
        infile = open(filename, "rb")
        inputpdf = PdfFileReader(infile, strict=False)

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("s_{0}-page{1}.pdf".format(filename.replace(".pdf",""), i), "wb") as outputStream:
                output.write(outputStream)
            outputStream.close()
        infile.close()  #find this take me a lot of time. It's close open pdf and only after it you can delete old files




def remove_old_files():
    os.chdir(path)
    for filename in os.listdir(path):
        if filename.startswith("scan"):
            os.remove(path + "\\" + filename)
