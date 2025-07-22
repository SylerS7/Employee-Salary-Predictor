from faker import Faker
import pandas as pd
import numpy as np
import random

fake = Faker('en_IN')  # Using Indian locale for more realistic names
num_rows = 10000

# Define constants with realistic mappings
education_levels = ["High School", "Bachelor's", "Master's", "PhD"]
industries = ["Information Technology", "Finance", "Healthcare", "Education", "Retail",
              "Telecommunications", "E-commerce", "Manufacturing", "Government", "Consulting"]

# Fixed location names with cost of living multipliers
locations = {
    "Mumbai": 1.2,
    "Bangalore": 1.1, 
    "Chennai": 0.95,
    "Delhi": 1.15,
    "Hyderabad": 0.9,
    "Pune": 1.0
}

# Employment type with realistic job titles and education requirements
employment_job_education = {
    "Internship": {
        "jobs": ["Software Development Intern", "Data Analytics Intern", "IT Support Intern", "Marketing Intern"],
        "min_education": ["High School", "Bachelor's"],
        "experience_range": (0, 1)
    },
    "Contract": {
        "jobs": ["Data Analyst", "Technical Support Engineer", "Software Engineer", "System Administrator", "DevOps Engineer", "Business Analyst"],
        "min_education": ["Bachelor's", "Master's"],
        "experience_range": (1, 8)
    },
    "Full-time": {
        "jobs": ["Machine Learning Engineer", "Data Analyst", "Cyber Security Analyst", "Data Scientist", 
                "System Administrator", "Data Engineer", "Senior Software Engineer", "Systems Engineer", 
                "Cloud Architect", "Software Engineer", "DevOps Engineer", "AI Researcher", "Full Stack Developer"],
        "min_education": ["Bachelor's", "Master's", "PhD"],
        "experience_range": (0, 20)
    }
}

# Industry-job compatibility matrix
industry_compatible_jobs = {
    "Information Technology": ["Machine Learning Engineer", "Data Analyst", "Cyber Security Analyst", "Data Scientist", 
                              "System Administrator", "Data Engineer", "Senior Software Engineer", "Systems Engineer", 
                              "Cloud Architect", "Software Engineer", "DevOps Engineer", "AI Researcher", "Full Stack Developer",
                              "Software Development Intern", "Data Analytics Intern", "IT Support Intern", "Technical Support Engineer", "Business Analyst"],
    "Finance": ["Data Analyst", "Cyber Security Analyst", "Data Scientist", "System Administrator", "Software Engineer",
               "Data Analytics Intern", "Business Analyst", "Technical Support Engineer"],
    "Healthcare": ["Data Analyst", "System Administrator", "Software Engineer", "IT Support Intern", "Technical Support Engineer"],
    "Education": ["Data Analyst", "System Administrator", "Software Engineer", "IT Support Intern", "Technical Support Engineer"],
    "Retail": ["Data Analyst", "System Administrator", "Software Engineer", "Marketing Intern", "Business Analyst"],
    "Telecommunications": ["Machine Learning Engineer", "Data Analyst", "Cyber Security Analyst", "System Administrator", 
                          "Senior Software Engineer", "Systems Engineer", "Software Engineer", "DevOps Engineer", 
                          "Technical Support Engineer", "IT Support Intern"],
    "E-commerce": ["Machine Learning Engineer", "Data Analyst", "Data Scientist", "Software Engineer", "Full Stack Developer",
                   "DevOps Engineer", "Software Development Intern", "Data Analytics Intern", "Business Analyst"],
    "Manufacturing": ["Data Analyst", "System Administrator", "Systems Engineer", "Software Engineer", "IT Support Intern"],
    "Government": ["Data Analyst", "Cyber Security Analyst", "System Administrator", "Software Engineer", "Technical Support Engineer"],
    "Consulting": ["Data Analyst", "Business Analyst", "Software Engineer", "Data Scientist", "Systems Engineer"]
}

# Education requirements for specific jobs
job_education_requirements = {
    "AI Researcher": ["Master's", "PhD"],
    "Machine Learning Engineer": ["Bachelor's", "Master's", "PhD"],
    "Data Scientist": ["Bachelor's", "Master's", "PhD"],
    "Cloud Architect": ["Bachelor's", "Master's"],
    "Senior Software Engineer": ["Bachelor's", "Master's"],
    "Cyber Security Analyst": ["Bachelor's", "Master's"]
}

# Base salaries in lakhs INR (more realistic)
job_base_salaries = {
    "Machine Learning Engineer": 15.0,
    "Data Analyst": 8.0,
    "Cyber Security Analyst": 12.0,
    "Data Scientist": 14.0,
    "System Administrator": 6.5,
    "Data Engineer": 11.0,
    "Senior Software Engineer": 18.0,
    "Systems Engineer": 7.5,
    "Cloud Architect": 22.0,
    "Software Engineer": 10.0,
    "DevOps Engineer": 13.0,
    "AI Researcher": 20.0,
    "Technical Support Engineer": 5.5,
    "Full Stack Developer": 12.0,
    "Business Analyst": 9.0,
    "Software Development Intern": 3.0,
    "Data Analytics Intern": 2.8,
    "IT Support Intern": 2.5,
    "Marketing Intern": 2.2
}

# Salary calculation with multiple factors
def generate_salary(job_title, education, experience, industry, location, gender, performance_factor):
    base = job_base_salaries.get(job_title, 8.0)
    
    # Education multiplier
    edu_multiplier = {
        "High School": 0.8,
        "Bachelor's": 1.0,
        "Master's": 1.25,
        "PhD": 1.5
    }.get(education, 1.0)
    
    # Industry multiplier
    industry_multipliers = {
        "Information Technology": 1.0,
        "Finance": 1.2,
        "Healthcare": 0.9,
        "Education": 0.75,
        "Retail": 0.8,
        "Telecommunications": 1.1,
        "E-commerce": 1.15,
        "Manufacturing": 0.85,
        "Government": 0.8,
        "Consulting": 1.25
    }
    industry_multiplier = industry_multipliers.get(industry, 1.0)
    
    # Experience multiplier (non-linear growth)
    if experience == 0:
        exp_multiplier = 0.8
    elif experience <= 2:
        exp_multiplier = 0.9 + (experience * 0.1)
    elif experience <= 5:
        exp_multiplier = 1.1 + ((experience - 2) * 0.15)
    elif experience <= 10:
        exp_multiplier = 1.55 + ((experience - 5) * 0.1)
    else:
        exp_multiplier = 2.05 + ((experience - 10) * 0.05)
    
    # Location multiplier
    location_multiplier = locations[location]
    
    # Gender pay gap (realistic modeling - unfortunately exists in real world)
    gender_multiplier = 0.92 if gender == 'Female' else 1.0
    
    # Performance factor (0.8 to 1.3)
    
    # Calculate final salary
    salary = base * edu_multiplier * exp_multiplier * industry_multiplier * location_multiplier * gender_multiplier * performance_factor
    
    # Add realistic variance
    variance = random.uniform(0.85, 1.2)
    final_salary = round(salary * variance, 2)
    
    return max(final_salary, 2.0)  # Minimum salary floor

# Generate realistic experience based on job level and age
def generate_experience(job_title, age, emp_type):
    if emp_type == "Internship":
        return random.randint(0, 1)
    
    max_possible_exp = max(0, age - 22)  # Assuming graduation at 22
    
    if "Senior" in job_title or "Architect" in job_title:
        min_exp = max(5, min(8, max_possible_exp))
        return min(random.randint(min_exp, min_exp + 10), max_possible_exp)
    elif "AI Researcher" in job_title:
        min_exp = max(3, min(5, max_possible_exp))
        return min(random.randint(min_exp, min_exp + 15), max_possible_exp)
    elif any(word in job_title for word in ["Engineer", "Developer", "Scientist"]):
        min_exp = max(0, min(2, max_possible_exp))
        return min(random.randint(min_exp, min_exp + 8), max_possible_exp)
    else:
        return min(random.randint(0, 6), max_possible_exp)

# Generate age based on experience and education
def generate_age(experience, education):
    graduation_age = {
        "High School": 18,
        "Bachelor's": 22,
        "Master's": 24,
        "PhD": 28
    }.get(education, 22)
    
    min_age = graduation_age + experience
    max_age = min(60, min_age + random.randint(0, 8))
    
    return random.randint(min_age, max_age)

# Check if job is compatible with industry
def is_job_industry_compatible(job_title, industry):
    return job_title in industry_compatible_jobs.get(industry, [])

# Check education requirements
def meets_education_requirements(job_title, education):
    if job_title in job_education_requirements:
        return education in job_education_requirements[job_title]
    return True

# Generate remote work probability based on job type and industry
def generate_remote_work(job_title, industry):
    # Higher probability for certain jobs
    remote_friendly_jobs = ["Software Engineer", "Data Analyst", "Full Stack Developer", 
                           "Machine Learning Engineer", "Data Scientist", "DevOps Engineer"]
    
    base_prob = 0.3  # Base 30% chance
    
    if any(job in job_title for job in remote_friendly_jobs):
        base_prob = 0.7
    elif "Support" in job_title or "Administrator" in job_title:
        base_prob = 0.2
    elif "Intern" in job_title:
        base_prob = 0.15
    
    # Industry adjustments
    if industry in ["Information Technology", "E-commerce", "Consulting"]:
        base_prob += 0.2
    elif industry in ["Manufacturing", "Healthcare", "Government"]:
        base_prob -= 0.2
    
    base_prob = max(0.05, min(0.85, base_prob))  # Keep between 5% and 85%
    
    return "Yes" if random.random() < base_prob else "No"

# Generate weekly hours based on job type and employment type
def generate_weekly_hours(emp_type, job_title):
    if emp_type == "Internship":
        return random.randint(20, 35)
    elif "Senior" in job_title or "Architect" in job_title:
        return random.randint(45, 55)
    else:
        return random.randint(38, 50)

# Generate certifications based on experience and job type
def generate_certifications(experience, job_title):
    base_certs = max(0, experience // 2)  # Roughly 1 cert per 2 years experience
    
    if any(word in job_title for word in ["Cyber", "Cloud", "DevOps"]):
        base_certs += random.randint(1, 3)
    elif "Data" in job_title or "AI" in job_title or "ML" in job_title:
        base_certs += random.randint(0, 2)
    
    return min(base_certs + random.randint(-1, 2), 8)  # Cap at 8 certifications

# Generate data with improved logic
data = []
attempts = 0
successful_records = 0

while successful_records < num_rows and attempts < num_rows * 3:
    attempts += 1
    
    # Basic demographics
    name = fake.name()
    gender = np.random.choice(['Male', 'Female'], p=[0.55, 0.45])  # Slightly more realistic distribution
    
    # Select employment type and compatible job
    emp_type = np.random.choice(list(employment_job_education.keys()), 
                               p=[0.05, 0.25, 0.70])  # Realistic distribution
    emp_info = employment_job_education[emp_type]
    
    # Select education level appropriate for employment type
    education = random.choice(emp_info["min_education"])
    if random.random() < 0.3:  # 30% chance of higher education
        edu_idx = education_levels.index(education)
        if edu_idx < len(education_levels) - 1:
            education = random.choice(education_levels[edu_idx:])
    
    # Select industry and compatible job
    industry = random.choice(industries)
    compatible_jobs = [job for job in emp_info["jobs"] 
                      if is_job_industry_compatible(job, industry)]
    
    if not compatible_jobs:
        continue  # Skip if no compatible jobs
    
    job_title = random.choice(compatible_jobs)
    
    # Check education requirements
    if not meets_education_requirements(job_title, education):
        continue
    
    # Generate experience and age
    temp_age = random.randint(22, 58)
    experience = generate_experience(job_title, temp_age, emp_type)
    age = generate_age(experience, education)
    
    # Validate age-experience relationship
    min_working_age = {"High School": 18, "Bachelor's": 22, "Master's": 24, "PhD": 28}[education]
    if age < min_working_age + experience:
        continue
    
    # Other attributes
    location = random.choice(list(locations.keys()))
    weekly_hours = generate_weekly_hours(emp_type, job_title)
    remote_work = generate_remote_work(job_title, industry)
    certifications = generate_certifications(experience, job_title)
    performance_factor = np.random.normal(1.0, 0.15)  # Normal distribution around 1.0
    performance_factor = max(0.8, min(1.3, performance_factor))  # Clamp between 0.8 and 1.3
    
    # Generate salary
    salary = generate_salary(job_title, education, experience, industry, 
                           location, gender, performance_factor)
    
    data.append({
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Education": education,
        "Job Title": job_title,
        "Experience": experience,
        "Employment Type": emp_type,  # Fixed spelling
        "Industry": industry,
        "Location": location,
        "Weekly Hours": weekly_hours,
        "Remote Work": remote_work,
        "Certifications": certifications,
        "Salary": salary
    })
    
    successful_records += 1

# Create DataFrame and export
df = pd.DataFrame(data)

# Add some final validation and cleanup
print(f"Dataset successfully generated with {len(df)} rows")
print(f"Generation attempts: {attempts}")
print(f"\nDataset Statistics:")
print(f"Average age: {df['Age'].mean():.1f}")
print(f"Average experience: {df['Experience'].mean():.1f}")
print(f"Average salary: {df['Salary'].mean():.1f} lakhs")
print(f"Remote work percentage: {(df['Remote Work'] == 'Yes').sum() / len(df) * 100:.1f}%")
print(f"Gender distribution: {df['Gender'].value_counts(normalize=True).round(2).to_dict()}")

# Export to CSV
df.to_csv("realistic_employee_dataset.csv", index=False)
print("\nDataset exported to 'realistic_employee_dataset.csv'")