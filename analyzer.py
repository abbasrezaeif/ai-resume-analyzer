from skills import TECH_SKILLS


def normalize_text(text):
    return text.lower()


def find_skills(resume_text):
    normalized_text = normalize_text(resume_text)

    found_skills = []

    for skill in TECH_SKILLS:
        if skill in normalized_text:
            found_skills.append(skill)

    return found_skills