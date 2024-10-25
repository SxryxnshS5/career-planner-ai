import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request, redirect, url_for
from app.utils import parse_cv, get_analysis
from app import prompts

# Load the .env file
_ = load_dotenv(find_dotenv())

# Flask app initialization
app = Flask(__name__)

# Configuration
model = "gpt-4o-mini"
temperature = 0.3
max_tokens = 2000  # Increase max_tokens to allow more detailed analysis

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'cv-file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['cv-file']
    job_role = request.form.get('job-role', '')

    if file.filename == '':
        return redirect(url_for('index'))

    # Parse the CV
    cv_text = parse_cv(file)

    # Prompts
    system_message = prompts.system_message
    prompt = prompts.generate_prompt(cv_text, job_role)

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    # Get analysis with increased token limit
    try:
        analysis = get_analysis(model, messages, temperature, max_tokens)
    except Exception as e:
        print(f"Error generating analysis: {e}")
        analysis = "We encountered an error while generating the analysis. Please try again later."

    return render_template('profile_assessment.html', analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)
