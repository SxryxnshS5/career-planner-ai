import os
from dotenv import load_dotenv, find_dotenv
from app.utils import parse_cv, get_analysis
from app import prompts

# Load the .env file
_ = load_dotenv(find_dotenv())

# Configuration
model = "gpt-4o-mini"
temperature = 0.3
max_tokens = 500

# Flask entry point
def main():
    pdf = "cv.pdf"
    cv_text = parse_cv(pdf)

    # Prompts
    system_message = prompts.system_message
    prompt = prompts.generate_prompt(cv_text, "software developer at google")

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    # Get analysis
    analysis = get_analysis(model, messages, temperature, max_tokens)
    print(analysis)

if __name__ == "__main__":
    main()
