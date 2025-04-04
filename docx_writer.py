from docx import Document
import tempfile
import os

def save_report_as_docx(report_text, filename="radiology_report.docx"):
    doc = Document()
    for line in report_text.strip().split("\n"):
        doc.add_paragraph(line)

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, filename)
    doc.save(file_path)
    return file_path
