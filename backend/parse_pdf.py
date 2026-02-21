import io
import re
from pypdf import PdfReader
from fastapi import UploadFile


def clean_extra_spaces(text: str) -> str:
    # Fixes character-spacing artifacts (e.g., "J o h a n n e s" -> "Johannes")
    text = re.sub(r'(?<=[a-zA-Z])\s(?=[a-zA-Z]\s)', '', text)
    # Collapse multiple newlines and extra whitespace
    text = re.sub(r'\n\s*\n', '\n', text)
    return text.strip()


async def parse_pdf(file: UploadFile) -> str:
    """
    Reads a FastAPI UploadFile, extracts the text from all pages,
    and returns a cleaned version of the text.
    """
    # Read the file content into memory
    content = await file.read()

    # Use BytesIO to allow pypdf to read the raw bytes
    pdf_stream = io.BytesIO(content)
    reader = PdfReader(pdf_stream)

    raw_text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            raw_text += extracted + "\n"

    # Apply the cleaning logic before returning
    return clean_extra_spaces(raw_text)