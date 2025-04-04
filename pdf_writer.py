from fpdf import FPDF
import uuid
import os

def save_report_as_pdf(report_text, output_dir=".", filename=None):
    if not filename:
        filename = f"radiology_report_{uuid.uuid4().hex[:8]}.pdf"

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in report_text.split("\n"):
        pdf.multi_cell(0, 10, line)

    file_path = os.path.join(output_dir, filename)
    pdf.output(file_path)
    return file_path
