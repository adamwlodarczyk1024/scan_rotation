import scanpreparation
# Function to rename multiple files
import time
def preparedata():
    scanpreparation.renamefiles("scan")
    scanpreparation.splitpdf()
    scanpreparation.remove_old_files()
    scanpreparation.renamefiles("mono")
# Driver Code
if __name__ == '__main__':

    # Calling main() function
    preparedata()

