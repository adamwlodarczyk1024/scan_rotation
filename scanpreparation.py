# Place where i make pdf transform
# i use this dataset https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DJHVHB
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import *
# PARAMETERS
path = "C:\\Users\\Adam\\Documents\\dane do ml\\pdf"
imgpath = "C:\\Users\\Adam\\Documents\\dane do ml\\jpg"
poppler = 'C:\\poppler-21.03.0\\Library\\bin'
path1= 'C:\\Users\\Adam\\PycharmProjects\\deep-image-orientation-angle-detection\\data\\dane\\180'
COUNT = 1
def rename_files(text):
    os.chdir(path1)


    def increment():
        global COUNT
        COUNT = COUNT + 1

    for f in os.listdir(path1):
        f_name, f_ext = os.path.splitext(f)
        f_name = "{0}{1}".format(text, COUNT)
        increment()

        new_name = '{}{}'.format(f_name, f_ext)
        os.rename(f, new_name)


def split_pdf():
    os.chdir(path)
    for filename in os.listdir(path):
        infile = open(filename, "rb")
        inputpdf = PdfFileReader(infile, strict=False)

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("s_{0}-page{1}.pdf".format(filename.replace(".pdf", ""), i), "wb") as outputStream:
                output.write(outputStream)
            outputStream.close()
        infile.close()


def remove_old_files():
    os.chdir(path)
    for filename in os.listdir(path):
        if filename.startswith("scan"):
            os.remove(path + "\\" + filename)


def pdf_to_img():
    os.chdir(path)
    for filename in os.listdir(path):
        print(path + "\\" + filename)
        pages = convert_from_path(path + "\\" + filename, size=(400, None), poppler_path=poppler)
        for page in pages:
            page.save(filename.replace(".pdf", ".jpg"), 'JPEG')
