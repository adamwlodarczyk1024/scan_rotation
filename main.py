
import scanpreparation
# Function to rename multiple files

def preparedata():
    scanpreparation.splitpdf()
    scanpreparation.remove_old_files()
    scanpreparation.renamefiles()
# Driver Code
if __name__ == '__main__':

    # Calling main() function
    preparedata()

