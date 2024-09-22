import PyPDF2
from resume_parser import ResumeParser
from job_recommendation import JobRecommendation
from ats_score import ResumeMatcher
pdf_path='C:/Users/91998/OneDrive/Documents/RESUME EVALUATOR CODE/uploads/priyanshi kanojia resume 1.pdf'
def extract_text_from_pdf(pdf_path):
    text=""
    with open(pdf_path,'rb') as file:
        reader=PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text
resume_data=extract_text_from_pdf(pdf_path)
'''
resume_parser=ResumeParser(resume_data)
name = resume_parser.extract_name_from_resume()
contact_number = resume_parser.extract_contact_number_from_resume()
email=resume_parser.extract_email_from_resume()
skills=resume_parser.extract_skills_from_resume()
print(f"Extracted Name: {name}")
print(f"Contact Number: {contact_number}")
print(f"Email: {email}")
print(f"Skills: {skills}")

job_recommender = JobRecommendation(resume_data)
recommended_job = job_recommender.recommend_job()
print("Recommended Job Role:", recommended_job)'''

job_description_text = '''Company Introduction
    {{Write a short and catchy paragraph about your company. Make sure to provide information about the company culture, perks, and benefits. Mention office hours, remote working possibilities, and everything else you think makes your company interesting.}}
    Job Description
    We are seeking a .NET developer responsible for building .NET applications using {{Insert specific .NET languages and technologies here that are relevant to your project; indicate whether the focus is on front-end, back-end, or both}}. Your primary responsibility will be to design and develop these layers of our applications, and to coordinate with the rest of the team working on different layers of the infrastructure. A commitment to collaborative problem solving, sophisticated design, and quality product is essential.
    Responsibilities
    - Translate application storyboards and use cases into functional applications
    - Design, build, and maintain efficient, reusable, and reliable code
    - Integrate data storage solutions {{may include databases, key-value stores, blob stores, etc.}}
    Skills
    - Strong knowledge of .NET web framework {{you may specify particular versions based on your requirements}}
    - Proficient in {{C# and/or VB.NET}}, with a good knowledge of their ecosystems
    - Familiarity with the Mono framework {{if needed}}'''
resume_matcher=ResumeMatcher(resume_data)
matching_score = resume_matcher.compute_matching_score(resume_data, job_description_text)
print(matching_score)

