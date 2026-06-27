from skills import TECH_SKILLS


def normalize_text(text):
    return text.lower()


def find_skills(text):
    normalized_text = normalize_text(text)

    found_skills = []

    for skill in TECH_SKILLS:
        if skill in normalized_text:
            found_skills.append(skill)

    return found_skills


def compare_skills(resume_skills, job_skills):
    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills


def calculate_match_score(matched_skills, job_skills):
    if len(job_skills) == 0:
        return 0

    score = (len(matched_skills) / len(job_skills)) * 100
    return round(score, 2)