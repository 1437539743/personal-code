import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def get_file(path, all_files):
    FileNames = os.listdir(path)
    for file_name in FileNames:
        cur_path = os.path.join(path, file_name)
        if os.path.isdir(cur_path):
            get_file(cur_path, all_files)
        else:
            if file_name.endswith('.pdf'):
                all_files.append(cur_path)
    return all_files


def extract_one_pdf(pdf_path, save_dir, start_page, end_page):
    pdf_name = os.path.basename(pdf_path)
    print(f"Processing file -- {pdf_path}")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    pdf_file = PdfFileReader(pdf_path, strict=False)
    pdf_pages = pdf_file.getNumPages()
    if not -1 < start_page < end_page < pdf_pages:
        raise ValueError("Pages Error")

    pdf_output = PdfFileWriter()
    for i in range(start_page, end_page):
        page = pdf_file.getPage(i)
        pdf_output.addPage(page)
    with open(os.path.join(save_dir, pdf_name), 'wb') as out:
        pdf_output.write(out)


def extract_many_pdf(pdf_dir_path, save_path, start_page, end_page):

    source_files = get_file(pdf_dir_path, [])
    for i, file in enumerate(source_files):
        file_name = os.path.basename(file)
        save_file = file.replace(pdf_dir_path, save_path)
        save_dir = save_file.replace(file_name, '')
        extract_one_pdf(file, save_dir, start_page, end_page)


if __name__ == '__main__':
    path = "C:\\Users\\Lenovo\\Desktop\\test\\"
    out_path = "C:\\Users\\Lenovo\\Desktop\\pdf_out\\"
    extract_many_pdf(path, out_path, 0, 1)
