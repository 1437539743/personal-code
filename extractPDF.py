import os
from PyPDF2 import PdfFileWriter, PdfFileReader


pdf_dir_path = "C:\\Users\\Lenovo\\Desktop\\pdf\\"
out_path = "C:\\Users\\Lenovo\\Desktop\\pdf_out\\"

if not os.path.exists(out_path):
    os.mkdir(out_path)

start_page, end_page = 0, 1

files = os.listdir(pdf_dir_path)
for f in files:

    output = PdfFileWriter()
    pdf_file = PdfFileReader(open(pdf_dir_path + f, "rb"))
    pdf_pages_len = pdf_file.getNumPages()

    # select pages
    for i in range(start_page, end_page):
        output.addPage(pdf_file.getPage(i))

    outputStream = open(out_path + f, "wb")
    output.write(outputStream)