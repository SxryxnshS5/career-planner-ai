
# Career Planner AI

## Overview
Career Planner AI is a Flask-based web application that helps users analyze their CVs and receive tailored career advice. Using OpenAI's GPT model, the application assesses user profiles and provides insights on strengths, weaknesses, and recommendations for achieving specific career goals.

## Features
- **CV Upload**: Users can upload their CVs in PDF format.
- **Goal Setting**: Users can enter their career goals (e.g., "Software Developer at Google") to receive specific feedback.
- **Analysis Results**: The application analyzes the CV and provides structured feedback, including strengths, weaknesses, recommendations, and a profile score.

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Firebase (will be implemented in future)
- **AI Integration**: OpenAI API (GPT-4o Mini)
- **File Handling**: PyPDF2 for extracting text from PDFs

## Live Demo
You can try out the live application here: [Career Planner AI](https://career-planner-ai.onrender.com/). 

**Note**: The site may take some time to load initially as Render spins down the site due to inactivity.

## Installation

### Prerequisites
- Python 3.6 or later
- pip (Python package installer)

### Setup
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd career-planner-ai
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup environment variables**: 
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-openai-api-key
   ```

## Running the Application
To start the Flask application, run the following command:
```bash
python app.py
```
Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage
1. Upload your CV in PDF format.
2. Enter your career goal.
3. Submit the form to receive an analysis of your profile.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss potential improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/) - Micro web framework for Python
- [OpenAI API](https://openai.com/api/) - API for interacting with OpenAI's models
- [PyPDF2](https://pythonhosted.org/PyPDF2/) - Library for PDF file handling

```

### Notes:
- Replace `<repository-url>` with the actual URL of your GitHub repository.
- If you have a `requirements.txt` file, make sure it's up to date with all the packages used in your project.
- Adjust any section based on your project’s specific details or any additional functionalities you may want to highlight. 

Feel free to customize this `README.md` further based on your preferences or additional features!
