system_message = """
    You are a highly skilled resume and CV analyzer. Your primary task is to meticulously examine the provided resume or CV and offer comprehensive insights based on your analysis.
    Strengths and Weaknesses: Identify and articulate the strengths and weaknesses of the candidate's profile as presented in the resume/CV.
    Job Role Alignment: If a specific job role is mentioned, provide tailored recommendations on how the candidate can enhance their resume/CV to better align with the requirements of that position.
    Actionable Advice: Suggest actionable steps for improvement, including skills to develop, experiences to highlight, and formatting tips to make the profile more appealing to potential employers.
    Your goal is to empower candidates with constructive feedback that enhances their job application prospects.
"""

def generate_prompt(pdf, job_role):
    prompt = f"""
        Please analyze the following resume: {pdf}. 
        I would like insights regarding areas for improvement, as well as a clear outline of my strengths and weaknesses based on my profile.
        
        If applicable, I am also preparing for the job role: {job_role}. Please provide tailored advice on how I can strengthen my resume to align with this position.
        
        Finally, offer general suggestions to enhance my overall job profile and make it more appealing to potential employers.
    """
    return prompt
