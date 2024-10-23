import os
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import app.prompts as prompts 

# load the .env file
_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
)

model = "gpt-4o-mini"
temperature = 0.3
max_tokens = 500

# cv
cv_text = ""
pdf = "cv.pdf"
with open(pdf, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)

    # Iterate through the range of total_pages
    for page_number in range(total_pages):
        page = reader.pages[page_number]
        cv_text += page.extract_text() + " "


# prompts
system_message = prompts.system_message
prompt = prompts.generate_prompt(cv_text, "software developer at google")

messages=[
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": prompt
            }
        ]

# helper function
def get_analysis():
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return completion.choices[0].message.content

print(get_analysis())