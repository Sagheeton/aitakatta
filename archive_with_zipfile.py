from zipfile import ZipFile

zip_ = ZipFile(r'resources/hello.zip')
unzip = zip_.namelist()

text = zip_.read('Hello.txt')
print(text)
# zip_.extractall('downloads')
# for u in unzip:
#     zip_.extract(u, 'downloads')
zip_.close()