import scanpreparation
# Function to rename multiple files


def preparedata():
    scanpreparation.rename_files("180_")
    # scanpreparation.split_pdf()
    # scanpreparation.remove_old_files()
    # scanpreparation.rename_files("mono")
    # scanpreparation.pdf_to_img()
# Driver Code


if __name__ == '__main__':
    preparedata()
