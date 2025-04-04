from llm_chain import generate_report_from_prompt
import re

def clean_response(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

def create_updated_report(user_prompt, selected_template):
    raw_response = generate_report_from_prompt(user_prompt, selected_template)
    cleaned_report = clean_response(raw_response)
    return cleaned_report
