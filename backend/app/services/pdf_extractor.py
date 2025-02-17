# # backend/app/services/pdf_extractor.py
# import PyPDF2
# import io

# def extract_text_from_pdf(file_content: bytes) -> str:
#     pdf_file = io.BytesIO(file_content)
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#     extracted_text = ""
#     for page in range(pdf_reader.numPages):
#         extracted_text += pdf_reader.getPage(page).extractText()
#     return extracted_text

from pdfminer.high_level import extract_text_to_fp
from io import BytesIO, StringIO

def extract_text_from_pdf(file_content: bytes) -> str:
    pdf_file = BytesIO(file_content)
    output_string = StringIO()
    extract_text_to_fp(pdf_file, output_string)
    return output_string.getvalue()