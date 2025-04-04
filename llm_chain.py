from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
import os

llm = ChatGroq(
    temperature=0.2,
    model_name=os.getenv("model_name"),
    api_key=os.getenv("GROQCLOUD_API_KEY")
)

def generate_report_from_prompt(user_prompt, template_text):
    messages = [
        SystemMessage(
            content=(
                "You're a radiologist assistant. Based on a given prompt describing radiological findings, "
                "you must update a normal radiology report template to reflect those findings. Use professional language."
            )
        ),
        HumanMessage(content=f"""Template:
            {template_text}

            Now, update the report based on this prompt:
            {user_prompt}

            Only output the final updated radiology report. Do not include any reasoning or thinking process."""
        )
    ]

    response = llm(messages)
    return response.content
