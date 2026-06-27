from analyzer import find_skills, compare_skills, calculate_match_score


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    resume_text = read_file("sample_resume.txt")
    job_description_text = read_file("sample_job_description.txt")

    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_description_text)

    matched_skills, missing_skills = compare_skills(resume_skills, job_skills)
    match_score = calculate_match_score(matched_skills, job_skills)

    print("AI Resume Analyzer")
    print("------------------")

    print("\nResume Skills:")
    for skill in resume_skills:
        print(f"- {skill}")

    print("\nJob Required Skills:")
    for skill in job_skills:
        print(f"- {skill}")

    print("\nMatched Skills:")
    for skill in matched_skills:
        print(f"- {skill}")

    print("\nMissing Skills:")
    for skill in missing_skills:
        print(f"- {skill}")

    print(f"\nMatch Score: {match_score}%")


if __name__ == "__main__":
    main()