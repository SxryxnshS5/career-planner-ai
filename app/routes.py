from flask import render_template, request, redirect, url_for
from app.utils import parse_cv, get_analysis  # Ensure utils.py is in the app package
from app import prompts  # Adjust for prompts being in the app package
from app.config import MODEL, TEMPERATURE, MAX_TOKENS  # Updated import path

def index():
    return render_template('index.html')

def analyze():
    if 'cv-file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['cv-file']
    job_role = request.form.get('job-role', '')

    if file.filename == '':
        return redirect(url_for('index'))

    # Parse the CV
    cv_text = parse_cv(file)

    # Prepare prompt and system message
    system_message = prompts.system_message
    prompt = prompts.generate_prompt(cv_text, job_role)
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    # Get analysis
    try:
        analysis = get_analysis(MODEL, messages, TEMPERATURE, MAX_TOKENS)
    except Exception as e:
        print(f"Error generating analysis: {e}")
        analysis = "We encountered an error while generating the analysis. Please try again later."

    return render_template('profile_assessment.html', analysis=analysis)
