import fitz, glob, os
import zipfile

def extract_upload():
    files = []
    for file in glob.glob("./zipfiles/*.zip"):
        files.append(file) 
    with zipfile.ZipFile(f"{files[0]}") as zObject:
        zObject.extractall("./merging_pdfs")
    os.remove(files[0])


def merge_files():
    files = []
    for file in glob.glob("./merging_pdfs/*.pdf"):
        files.append(file) 
    result = fitz.open()
    for pdf in files:
        with fitz.open(pdf) as mfile:
            result.insert_pdf(mfile)
        os.remove(pdf)
    result.save("./merged_pdf/result.pdf")



if __name__ == "__main__":
    extract_upload()
    merge_files()