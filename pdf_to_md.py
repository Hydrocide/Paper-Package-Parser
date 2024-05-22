import os

from PIL import Image
import pymupdf4llm
import pathlib

import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\andrew\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\pytesseract\pytesseract.py'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Define the folder path containing the PNG files
folder_path = r'C:\Users\andrew\Desktop\Python Projects\Paper Package Parser\PDFs'

import time

start_time = time.time()
# Iterate through all files in the folder
for file_name in os.listdir(folder_path):

    # convert the document to markdown
    if "single" in file_name: continue 
    md_text = pymupdf4llm.to_markdown(f"{folder_path}\{file_name}")
    print(md_text)
    # Write the text to some file in UTF8-encoding
    file_name = file_name.replace(".pdf","")        ################    UNTESTED    TODO: TEST
    pathlib.Path(f"Markdowns\{file_name}.md").write_bytes(md_text.encode())

end_time = time.time()



elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")

#print((elapsed_time * 775)/60) # EXPECTED - 377s ~ 5 minutes 45 seconds