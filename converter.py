"""
Convert scanned PDFs to a text-extractable format

Andrew Kotyck
22/5/2024
"""


import fitz

test_filepath = r"C:\Users\andrew\Desktop\testdoc.pdf"


import sys, pathlib, pymupdf
# with pymupdf.open(test_filepath, filetype="txt") as doc:  # open document
#     print([page.get_text() for page in doc])

# doc = fitz.open(test_filepath)
# page = doc.load_page(0)
# pixmap = page.get_pixmap(dpi=300)
# img = pixmap.tobytes()


doc = fitz.open(test_filepath)
for page in doc:  # iterate through the pages
    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = pymupdf.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
    pix = page.get_pixmap(matrix=mat)  # use 'mat' instead of the identity matrix
    pix.save("images/page-%i.png" % page.number)  # store image as a PNG



# def loadscanned(filepath: str) -> None:
#     pass

