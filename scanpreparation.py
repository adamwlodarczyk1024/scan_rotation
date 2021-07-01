# Place where i make pdf transform
# i use this dataset https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DJHVHB
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

# place where you have pdf multiscan
path = "C:\\Users\\Adam\\Documents\\dane do ml\\pdf"
COUNT = 1

def renamefiles():

    os.chdir(path)


    # Function to increment count
    # to make the files sorted.
    def increment():
        global COUNT
        COUNT = COUNT + 1

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        f_name = "scans" + str(COUNT)
        increment()

        new_name = '{} {}'.format(f_name, f_ext)
        os.rename(f, new_name)



def splitpdf():
    os.chdir(path)
    for filename in os.listdir(path):

        inputpdf = PdfFileReader(open(filename, "rb"))

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("document-{0}-page{1}.pdf".format(filename, i), "wb") as outputStream:
                output.write(outputStream)


def remove_old_files():
    os.chdir(path)
    for filename in os.listdir(path):
        os.remove(path + "\\" + filename)

