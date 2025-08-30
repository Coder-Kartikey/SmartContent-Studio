import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
import os

import pdfkit
from docx import Document

import time

load_dotenv()
genai_Api_Key = st.secrets["API_KEY"]

genai.configure(api_key=genai_Api_Key)

generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 1024,
        "response_mime_type": "text/plain",
}

def generate_resume(name, job_title, skills, experience_title, experience_company, experience_start_date, experience_end_date, experience_description, education_degree, education_major, education_university, education_start_date, education_end_date, template, custom_prompt):
        model=genai.GenerativeModel(
                model_name="gemini-1.5-pro",
                generation_config=generation_config,
        )

        if template == "Basic":
            promt_prefix = "Please generate a basic resume based on the following information:"
        elif template == "Professional":
            promt_prefix = "Please generate a professional resume based on the following information:"
        elif template == "Modern":
            promt_prefix = "Please generate a modern resume based on the following information:"
        elif template == "Creative":
            promt_prefix = "Please generate a creative resume based on the following information:"
        elif template == "Elegant":
            promt_prefix = "Please generate an elegant resume based on the following information:"
        elif template == "Executive":
            promt_prefix = "Please generate an executive resume based on the following information:"
        elif template == "Classic":
            promt_prefix = "Please generate a classic resume based on the following information:"
        elif template == "Simple":
            promt_prefix = "Please generate a simple resume based on the following information:"
        elif template == "Minimalist":
            promt_prefix = "Please generate a minimalist resume based on the following information:"
        elif template == "Stylish":        
            promt_prefix = "Please generate a stylish resume based on the following information:"
        elif template == "Sophisticated":
            promt_prefix = "Please generate a sophisticated resume based on the following information:"
        elif template == "Traditional":
            promt_prefix = "Please generate a traditional resume based on the following information:"
        elif template == "Contemporary":
            promt_prefix = "Please generate a contemporary resume based on the following information:"
        elif template == "Futuristic":
            promt_prefix = "Please generate a futuristic resume based on the following information:"
        elif template == "Artistic":
            promt_prefix = "Please generate an artistic resume based on the following information:"
        elif template == "Colorful":
            promt_prefix = "Please generate a colorful resume based on the following information:"
        elif template == "Bold":
            promt_prefix = "Please generate a bold resume based on the following information:"
        elif template == "Unique":
            promt_prefix = "Please generate a unique resume based on the following information:"
        elif template == "Custom":
            promt_prefix = "Please generate a custom resume based on the following information:"

        context = f"{promt_prefix}\nName: {name}\nJob Title: {job_title}\nSkills: {', '.join(skills)}\nExperience: {experience_title} at {experience_company} ({experience_start_date} - {experience_end_date})\nDescription: {experience_description}\nEducation: {education_degree} in {education_major} from {education_university} ({education_start_date} - {education_end_date})\n{custom_prompt}"
        chat_session = model.start_chat(
                history=[
                        {
                                "role": "user",
                                "parts": [
                                        context
                                ],
                        }
                ],
        )

        response = chat_session.send_message(context)

        # text = response.candidates[0].content if isinstance(response.candidates[0].content, str) else response.candidates[0].content.text
        text = response.candidates[0].content.parts[0].text

        return text

def clean_resume_text(text):
        replacements = {
                "[Add Email Address]": "[Your Email Address]",
                "[Add Phone Number]": "[Your Phone Number]",
                "[Add LinkedIn Profile]": "[Your LinkedIn Profile]",
                "[Add University Name]": "[Your University Name]",
                "[Add Graduation Year]": "[Your Graduation Year]",
        }
        for old, new in replacements.items():
                text = text.replace(old, new)
        return text

def create_pdf_download_link(text, filename="resume.pdf"):
    pdf = pdfkit.from_string(text, False)
    st.markdown(f'<a href="data:application/pdf;base64,{pdf.decode("utf-8")}" download="{filename}">Download PDF</a>', unsafe_allow_html=True)

def create_docx_download_link(text, filename="resume.docx"):
    document = Document()
    document.add_paragraph(text)
    document.save("resume.docx")
    with open("resume.docx", "rb") as file:
        docx_data = file.read()
    st.download_button(
        label="Download DOCX",
        data=docx_data,
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
st.set_page_config(
    page_title="SmartContent Studio",
    page_icon=":briefcase:",
#     layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com',
        'Report a bug': "https://www.example.com",
        'About': "This is a SmartContent Studio app!"
    }
)

st.title("SmartContent Studio")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Enter your full name")
with col2:
    job_title = st.text_input("Enter your job title")
skills = st.multiselect("Enter your skills", ["Python", "Machine Learning", "Deep Learning", "Data Science", "Software Development", "Web Development", "Cloud Computing", "DevOps", "Cybersecurity", "Blockchain", "IoT", "Big Data", "Data Analytics", "Data Engineering", "Data Visualization", "Business Intelligence", "Artificial Intelligence", "Natural Language Processing", "Computer Vision", "Robotics", "Automation", "Quantum Computing", "Augmented Reality", "Virtual Reality", "Game Development", "Mobile Development", "Desktop Development", "Backend Development", "Frontend Development", "Full Stack Development", "Database Management", "System Administration", "Network Administration", "IT Support", "Technical Support", "Customer Support", "Sales", "Marketing", "Product Management", "Project Management", "Quality Assurance", "Testing", "Technical Writing", "Content Writing", "Copywriting", "Blogging", "SEO", "SEM", "Social Media Marketing", "Email Marketing", "Affiliate Marketing", "Influencer Marketing", "Growth Hacking", "Digital Marketing", "E-commerce", "Dropshipping", "Freelancing", "Entrepreneurship", "Startup", "Venture Capital", "Private Equity", "Investment Banking", "Finance", "Accounting", "Economics", "Business Analysis", "Business Development", "Consulting", "Legal", "Human Resources", "Recruitment", "Training", "Learning & Development", "Employee Relations", "Organizational Development", "Change Management", "Performance Management", "Compensation & Benefits", "Payroll", "Talent Management", "Diversity & Inclusion", "Employee Engagement", "Workforce Planning", "Succession Planning", "HRIS", "People Analytics", "Health & Safety", "Wellness", "Occupational Health", "Employee Assistance", "Labor Relations", "Union Negotiations", "Employment Law", "Regulatory Compliance", "Risk Management", "Insurance", "Claims", "Underwriting", "Actuarial", "Investments", "Wealth Management", "Financial Planning", "Retirement Planning", "Tax Planning", "Estate Planning", "Trusts & Estates", "Philanthropy", "Charitable Giving", "Social Impact", "Sustainability", "Corporate Social Responsibility", "Environmental, Social, Governance", "Ethics", "Compliance", "Anti-Money Laundering", "Fraud Prevention", "Cybersecurity", "Information Security", "Privacy", "Data Protection", "GDPR", "CCPA", "HIPAA", "PCI DSS", "SOX", "ISO 27001", "NIST", "CIS", "CMMC", "ITIL", "COBIT", "Agile", "Scrum", "Kanban", "Lean", "Six Sigma", "Kaizen", "Total Quality Management"])
with st.expander("Experience"):
    col_exp1, col_exp2 = st.columns(2)
    with col_exp1:
        experience_title = st.text_input("Title")
    with col_exp2:
        experience_company = st.text_input("Company")
    with col_exp1:
        experience_start_date = st.text_input("Start date")
    with col_exp2:
        experience_end_date = st.text_input("End date")
    experience_description = st.text_area("Description")
with st.expander("Education"):
    col_edu1, col_edu2 = st.columns(2)
    col_edu3, col_edu4 = st.columns(2)
    with col_edu1:
        education_degree = st.text_input("Degree")
    with col_edu2:
        education_major = st.text_input("Major")
    education_university = st.text_input("University")
    with col_edu3:
        education_start_date = st.text_input("Admission date")
    with col_edu4:
        education_end_date = st.text_input("Passout date")
template = st.selectbox("Select a resume template", ["Basic", "Professional", "Modern", "Creative", "Elegant", "Executive", "Classic", "Simple", "Minimalist", "Stylish", "Sophisticated", "Traditional", "Contemporary", "Futuristic", "Artistic", "Colorful", "Bold", "Unique", "Custom"])
custom_prompt = st.text_area("Enter any additional information or custom prompt")

if st.button("Generate Resume"):
        if name and job_title and skills and experience_title and experience_company and experience_start_date and experience_end_date and experience_description and education_degree and education_major and education_university and education_start_date and education_end_date and template and custom_prompt:
                my_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.5)
                    my_bar.progress(percent_complete + 1)
                try:
                        resume = generate_resume(name, job_title, skills, experience_title, experience_company, experience_start_date, experience_end_date, experience_description, education_degree, education_major, education_university, education_start_date, education_end_date, template, custom_prompt)
                        cleaned = clean_resume_text(resume)
                        st.markdown("#### Generated Resume")
                        st.write(cleaned)

                        # create_pdf_download_link(cleaned)
                        create_docx_download_link(cleaned)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
                st.warning("Please enter all the data!")