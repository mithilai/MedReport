from llm_chain import generate_report_from_prompt
import re

def load_template(path="templates/mri_brain.txt"):
    with open(path, "r") as file:
        return file.read()

def clean_response(text):
    # Remove <think>...</think> and trim spaces
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

def create_updated_report(user_prompt):
    template = load_template()
    raw_response = generate_report_from_prompt(user_prompt, template)
    cleaned_report = clean_response(raw_response)
    return cleaned_report
