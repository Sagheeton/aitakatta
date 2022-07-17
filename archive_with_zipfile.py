from zipfile import ZipFile
from pathlib import Path

pdf_file_name = 'latest.pdf'
xlsx_file_name = 'file_example_XLSX_50.xlsx'
csv_file_name = 'username.csv'


Path('/resources').mkdir(parents=True, exist_ok=True)

# zippy = ZipFile(r'resources/zippy.zip', 'w')
#
# zippy.write(pdf_file_name)
# zippy.write(xlsx_file_name)
# zippy.write(csv_file_name)




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