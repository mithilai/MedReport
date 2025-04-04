import streamlit as st
from report_generator import create_updated_report
from pdf_writer import save_report_as_pdf
from docx_writer import save_report_as_docx
from ct_template import (
    CT_ABDO_PELVIS_MALE_NORMAL,
    CT_ABDO_PELVIS_FEMALE_NORMAL,
    MRI_BRAIN_IW_NORMAL,
    MRI_LS_SPINE_NORMAL
)
import tempfile
import os

st.set_page_config(page_title="Radiologist Assistant", layout="centered")
st.title("🧠 Radiologist Report Assistant")

# UI inputs
patient_name = st.text_input("Patient Name")
report_date = st.date_input("Report Date")
user_prompt = st.text_area("Enter radiology findings:", height=200)

template_option = st.selectbox("Choose a report template", [
    "CT Abdomen & Pelvis - Male",
    "CT Abdomen & Pelvis - Female",
    "MRI Brain Plain",
    "MRI LS Spine"
])

# Load selected template
template_map = {
    "CT Abdomen & Pelvis - Male": CT_ABDO_PELVIS_MALE_NORMAL,
    "CT Abdomen & Pelvis - Female": CT_ABDO_PELVIS_FEMALE_NORMAL,
    "MRI Brain Plain": MRI_BRAIN_IW_NORMAL,
    "MRI LS Spine": MRI_LS_SPINE_NORMAL
}
selected_template_text = template_map[template_option]

# Session state
if "report_text" not in st.session_state:
    st.session_state.report_text = ""
if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = ""
if "docx_path" not in st.session_state:
    st.session_state.docx_path = ""

# Generate report
if st.button("Generate Report"):
    if user_prompt.strip():
        with st.spinner("Generating report..."):
            report = create_updated_report(user_prompt, selected_template_text)
            report = report.replace("[To be filled]", "").strip()
            report = report.replace("Patient:", f"Patient: {patient_name or 'N/A'}")
            report = report.replace("Date:", f"Date: {report_date.strftime('%d-%m-%Y') if report_date else 'N/A'}")

            st.session_state.report_text = report
            st.session_state.pdf_path = ""
            st.session_state.docx_path = ""
    else:
        st.warning("Please enter a prompt.")

# Report preview and download
if st.session_state.report_text:
    st.text_area("📋 Report Preview:", value=st.session_state.report_text, height=400)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄 Create PDF"):
            with st.spinner("Saving PDF..."):
                filename = f"{patient_name or 'report'}_{report_date.strftime('%d-%m-%Y')}.pdf"
                st.session_state.pdf_path = save_report_as_pdf(st.session_state.report_text, filename)
                

    with col2:
        if st.button("📝 Create DOCX"):
            with st.spinner("Saving DOCX..."):
                filename = f"{patient_name or 'report'}_{report_date.strftime('%d-%m-%Y')}.docx"
                st.session_state.docx_path = save_report_as_docx(st.session_state.report_text, filename)

    if st.session_state.pdf_path:
        with open(st.session_state.pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download PDF",
                data=f,
                file_name=os.path.basename(st.session_state.pdf_path),
                mime="application/pdf"
            )

    if st.session_state.docx_path:
        with open(st.session_state.docx_path, "rb") as f:
            st.download_button(
                label="⬇️ Download DOCX",
                data=f,
                file_name=os.path.basename(st.session_state.docx_path),
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
