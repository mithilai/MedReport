from docx import Document
import os

# File paths from uploaded documents
file_paths = {
    "ct_abdomen_male": "docs\CT - PLAIN ABDOMEN & PELVIS - MALE -- normal.docx",
    "ct_abdomen_female": "docs\CT - PLAIN ABDOMEN & PELVIS - FEMALE --.docx",
    "mri_brain": "docs\MRI BRAIN - IW - NORMAL--.docx",
    "mri_ls_spine": "docs\MRI LS SPINE --.docx",
}

# Function to extract text from .docx file
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

# Extracted texts from all templates
extracted_templates = {name: extract_text_from_docx(path) for name, path in file_paths.items()}
extracted_templates.keys()  # Show the available template categories extracted
