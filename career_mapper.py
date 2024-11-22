def map_careers(skills):
    # Simplified mapping logic
    career_map = {
        "Programming": ["Software Engineer", "Web Developer"],
        "Biology": ["Research Scientist", "Lab Technician"],
    }
    matched_careers = []
    for skill in skills:
        for key, careers in career_map.items():
            if key.lower() in skill.lower():
                matched_careers.extend(careers)
    return list(set(matched_careers))

