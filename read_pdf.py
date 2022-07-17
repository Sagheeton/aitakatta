from PyPDF2 import PdfReader

def test_pdf_number_of_pages():
    reader = PdfReader('resources/latest.pdf')
    numer_of_pages = len(reader.pages)
    assert numer_of_pages == 412, 'В файле не 412 страниц'

    page = reader.pages[0]
    text = page.extract_text()
    assert '2022' in text, 'На первой странице нет текста 2022'