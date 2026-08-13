# AI Resume Analyzer

print("🤖 AI Resume Analyzer")
print("---------------------")

resume = input("Paste your resume text below:\n\n")

print("\n🔍 Analyzing your resume...")
print("---------------------------")

# Basic checks
skills = ["python", "java", "c++", "sql", "machine learning", "ai", "git"]
found_skills = []

resume_lower = resume.lower()

for skill in skills:
    if skill in resume_lower:
        found_skills.append(skill)

# Display results
print("\n📊 Analysis Results")

print(f"Resume length: {len(resume.split())} words")

if found_skills:
    print("\n🛠️ Skills detected:")
    for skill in found_skills:
        print(f"- {skill}")
else:
    print("\n⚠️ No technical skills detected.")

# Basic suggestions
print("\n💡 Suggestions:")

if len(resume.split()) < 100:
    print("- Your resume may be too short. Consider adding projects or relevant experience.")

if len(found_skills) < 3:
    print("- Consider adding relevant technical skills that you genuinely know.")

if "project" not in resume_lower:
    print("- Consider adding a Projects section with your GitHub projects.")

if "education" not in resume_lower:
    print("- Consider adding an Education section.")

print("\n✅ Analysis complete!")
