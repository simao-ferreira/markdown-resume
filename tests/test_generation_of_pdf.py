from os import remove
from os.path import exists

from create_pdf import pdf_resume

PDF_FILE = f'./../output/resume*.pdf'


def setup_function():
    """Remove PDF file if exists"""

    if exists(PDF_FILE):
        remove(PDF_FILE)


# def test_generate_pdf_from_defaults():
#     assert not exists(PDF_FILE)
#
#     pdf_resume()
#     assert exists(PDF_FILE)
