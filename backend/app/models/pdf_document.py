# backend/app/models/pdf_document.py
from pydantic import BaseModel

class PDFDocument(BaseModel):
    filename: str
    extracted_text: str