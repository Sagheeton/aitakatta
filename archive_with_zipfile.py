import os
from pathlib import Path
from zipfile import ZipFile
from read_pdf import test_pdf_number_of_pages as check_pdf_pages
from read_xlsx import test_some_cell_value
from read_csv import test_some_value

pdf_file_name = 'latest.pdf'
xlsx_file_name = 'file_example_XLSX_50.xlsx'
csv_file_name = 'username.csv'

current_directory = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(current_directory, 'resources')
Path(path).mkdir(parents=True, exist_ok=True)

zippy = ZipFile(os.path.join(path, 'zippy.zip'), 'w')

zippy.write(pdf_file_name)
zippy.write(xlsx_file_name)
zippy.write(csv_file_name)

zippy.extract(pdf_file_name, r'tmp/')
check_pdf_pages(fr'tmp/{pdf_file_name}')

zippy.extract(xlsx_file_name, r'tmp/')
test_some_cell_value(fr'tmp/{xlsx_file_name}')

zippy.extract(csv_file_name, r'tmp/')
test_some_value(fr'tmp/{csv_file_name}')




# zippy.close()
# zip_ = ZipFile(r'files/hello.zip')
# unzip = zip_.namelist()
#
# text = zip_.read('Hello.txt')
# print(text)
# # zip_.extractall('downloads')
# # for u in unzip:
# #     zip_.extract(u, 'downloads')
# zip_.close()