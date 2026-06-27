from analyzer import find_skills


def read_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    resume_text = read_resume("sample_resume.txt")
    found_skills = find_skills(resume_text)

    print("AI Resume Analyzer")
    print("------------------")

    if found_skills:
        print("Skills found in resume:")
        for skill in found_skills:
            print(f"- {skill}")
    else:
        print("No skills found.")


if __name__ == "__main__":
    main()