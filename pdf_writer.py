from fpdf import FPDF
import tempfile
import os

def save_report_as_pdf(report_text, filename="radiology_report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in report_text.split("\n"):
        pdf.multi_cell(0, 10, line)

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, filename)
    pdf.output(file_path)
    return file_path
