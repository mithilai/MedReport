import streamlit as st
from report_generator import create_updated_report
from pdf_writer import save_report_as_pdf
import tempfile
import os

st.set_page_config(page_title="Radiologist Assistant", layout="centered")
st.title("🧠 Radiologist Report Assistant")

# Input fields
patient_name = st.text_input("Patient Name")
report_date = st.date_input("Report Date")
user_prompt = st.text_area("Enter radiology findings:", height=200, placeholder="e.g. make a report of MRI brain plain...")

# Session state to store generated report
if "report_text" not in st.session_state:
    st.session_state.report_text = ""
if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = ""

# Generate report button
if st.button("Generate Report"):
    if user_prompt.strip():
        with st.spinner("Generating report..."):
            final_report = create_updated_report(user_prompt)

            # Fill in name/date
            final_report = final_report.replace("[To be filled]", "").strip()
            final_report = final_report.replace("Patient:", f"Patient: {patient_name or 'N/A'}")
            final_report = final_report.replace("Date:", f"Date: {report_date.strftime('%d-%m-%Y') if report_date else 'N/A'}")

            # Store the report in session
            st.session_state.report_text = final_report
            st.session_state.pdf_path = ""  # Reset PDF path until user downloads
    else:
        st.warning("Please enter a prompt to generate a report.")

# Show preview if report is generated
if st.session_state.report_text:
    st.text_area("📋 Report Preview:", value=st.session_state.report_text, height=400)

    # Button to download PDF
    if st.button("📄 Create PDF"):
        # Save PDF only when this button is clicked
        with st.spinner("Creating PDF..."):
            pdf_path = save_report_as_pdf(st.session_state.report_text)
            st.session_state.pdf_path = pdf_path

    # Show download button if PDF path exists
    if st.session_state.pdf_path:
        with open(st.session_state.pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Click to Download PDF",
                data=f,
                file_name=os.path.basename(st.session_state.pdf_path),
                mime="application/pdf"
            )
