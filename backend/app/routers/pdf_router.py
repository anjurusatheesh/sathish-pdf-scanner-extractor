# backend/app/routers/pdf_router.py
from fastapi import APIRouter, File, UploadFile
#from services import pdf_extractor, s3_service, mongodb_service
from app.services import pdf_extractor, s3_service, mongodb_service
# from models.pdf_document import PDFDocument
from app.models.pdf_document import PDFDocument


router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    
    extracted_text = pdf_extractor.extract_text_from_pdf(contents)
    
    document = PDFDocument(filename=file.filename, extracted_text=extracted_text)
    mongodb_service.insert_document(document.dict())
    
    s3_upload_success = s3_service.upload_to_s3(contents, file.filename)
    
    return {"message": "File processed", "s3_upload": s3_upload_success, "extracted_text": extracted_text}