# SmartResume Generator

SmartResume Generator is an AI-powered platform designed to simplify resume creation. Using generative AI technology, this tool creates professional, tailored resumes based on user inputs. With multiple customizable templates and the ability to generate resumes in PDF and DOCX formats, users can save time, reduce stress, and ensure their resumes stand out in job applications.

---

## Features

- **Generative AI for Resume Creation**: Automatically generates high-quality resume content based on user-provided information and custom prompts.
- **Interactive User Interface**: A user-friendly platform built with Streamlit for easy navigation and data input.
- **Customizable Resume Templates**: Choose from a wide range of professional templates to match your style and industry.
- **Multi-Format Downloads**: Export resumes in both PDF and DOCX formats for flexibility and convenience.
- **Real-Time Progress Updates**: Visual progress indicator ensures a seamless user experience.
- **Secure Data Handling**: API keys and sensitive user inputs are securely managed using environment variables.

---

## Installation

To set up and run the SmartResume Generator locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/smartresume-generator.git
   cd smartresume-generator

2. **Install Dependencies: Ensure you have Python installed. Install the required libraries:**:
   ```bash
   pip install -r requirements.txt

3. **Set Up Environment Variables**:
   - Create a .env file in the root directory.
   - Add your API key:
        ```
        API_KEY=your_google_generative_ai_api_key

4. **Run the Application: Start the application locally using Streamlit**:
    ```bash
    streamlit run app.py

5. **Access the Application**: Open your browser and navigate to
    ```
    [http://localhost:8501](http://localhost:8501)

## Usage

1. Enter personal details such as name, job title, and skills.

2. Provide your professional and educational experience.

3. Select a resume template from various available options.

4. Input a custom prompt for additional customization.

5. Click "Generate Resume" and review the generated content.

6. Download your resume in PDF or DOCX format.

## Technology Stack

- **Frontend**: Streamlit

- **Backend**: Python

- **AI Engine**: Google Generative AI (Gemini-1.5-pro)

- **Template Management**: Pre-designed HTML/CSS layouts

- **File Conversion**: pdfkit (PDF) and python-docx (DOCX)

## Contribution

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## Contact

For questions, suggestions, or feedback, please contact us at:

- **E-mail**: ```pkartikey5757@gmail.com

# Author

CoderKP