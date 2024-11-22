career_map = {
    "Python": ["Data Scientist", "Software Developer"],
    "Machine Learning": ["AI Engineer", "ML Researcher"],
    "Marketing": ["Marketing Specialist", "Brand Manager"]
}

def map_skills_to_careers(skills):
    careers = []
    for skill in skills:
        if skill in career_map:
            careers.extend(career_map[skill])
    return list(set(careers))  # Remove duplicates

