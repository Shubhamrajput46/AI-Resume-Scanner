import os
import PyPDF2
import pandas as pd
import numpy as np

# Required Skills
required_skills = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "machine learning",
    "communication"
]

# Resume folder
resume_folder = "resumes"

results = []

# Function to extract text from PDF

def extract_text(pdf_path):

    text = ""

    with open(pdf_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text.lower()

# Resume Scoring Function

def calculate_score(text):

    matched_skills = 0

    found_skills = []

    for skill in required_skills:

        if skill in text:
            matched_skills += 1
            found_skills.append(skill)

    score = (matched_skills / len(required_skills)) * 100

    return round(score, 2), found_skills

# Scan All Resumes

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        path = os.path.join(resume_folder, file)

        resume_text = extract_text(path)

        score, skills = calculate_score(resume_text)

        results.append({
            "Resume": file,
            "Score": score,
            "Skills Found": ", ".join(skills),
            "Status": "Shortlisted" if score >= 60 else "Rejected"
        })

# Create DataFrame
df = pd.DataFrame(results)

# Sort by score
df = df.sort_values(by="Score", ascending=False)

# Display results
print(df)

# Save CSV
df.to_csv("output/resume_results.csv", index=False)

print("\nResults saved successfully!")