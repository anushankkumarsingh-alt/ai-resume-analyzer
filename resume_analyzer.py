# AI Resume Analyzer

print("🤖 AI Resume Analyzer")
print("---------------------")

resume = input("Paste your resume text below:\n\n")

resume_lower = resume.lower()
word_count = len(resume.split())

print("\n🔍 Analyzing your resume...")
print("---------------------------")

# Technical skills
skills = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "ai",
    "git",
    "github"
]

found_skills = []

for skill in skills:
    if skill in resume_lower:
        found_skills.append(skill)

# Resume sections
sections = {
    "Education": ["education", "academic"],
    "Experience": ["experience", "internship", "intern"],
    "Projects": ["projects", "project"],
    "Skills": ["skills", "technical skills"],
    "Certifications": ["certification", "certifications", "certificate"],
    "Contact": ["email", "phone", "linkedin"]
}

found_sections = []
missing_sections = []

for section, keywords in sections.items():
    found = False

    for keyword in keywords:
        if keyword in resume_lower:
            found = True
            break

    if found:
        found_sections.append(section)
    else:
        missing_sections.append(section)

# Calculate a basic score
score = 0

# Resume length
if 200 <= word_count <= 800:
    score += 20
elif 100 <= word_count < 200 or 800 < word_count <= 1000:
    score += 10

# Technical skills
if len(found_skills) >= 5:
    score += 20
elif len(found_skills) >= 3:
    score += 15
elif len(found_skills) >= 1:
    score += 10

# Resume sections
score += min(len(found_sections) * 10, 60)

# Keep score within 100
score = min(score, 100)

# Results
print("\n📊 Analysis Results")
print("-------------------")
print(f"Resume length: {word_count} words")

print("\n🛠️ Technical Skills Detected:")

if found_skills:
    for skill in found_skills:
        print(f"- {skill}")
else:
    print("- No listed technical skills detected.")

print("\n📂 Resume Sections Found:")

if found_sections:
    for section in found_sections:
        print(f"✅ {section}")
else:
    print("- No common resume sections detected.")

print("\n⚠️ Sections You May Want to Add:")

if missing_sections:
    for section in missing_sections:
        print(f"- {section}")
else:
    print("🎉 All basic sections were detected!")

# Score
print("\n🏆 Resume Score")
print("---------------")
print(f"Score: {score}/100")

if score >= 80:
    print("🌟 Strong basic structure!")
elif score >= 60:
    print("👍 Good start. A few improvements could make it stronger.")
elif score >= 40:
    print("📈 Your resume has a foundation, but it could use improvement.")
else:
    print("🔧 Your resume needs more structure and relevant content.")

# Suggestions
print("\n💡 Suggestions")
print("--------------")

if word_count < 100:
    print("- Your resume may be too short. Add relevant projects, education, or experience.")

if word_count > 1000:
    print("- Your resume may be too long. Remove unnecessary information.")

if len(found_skills) < 3:
    print("- Add relevant technical skills that you genuinely know.")

if "project" not in resume_lower:
    print("- Add a Projects section with your strongest projects.")

if "github" not in resume_lower:
    print("- Consider adding your GitHub profile or relevant project links.")

print("\n✅ Analysis complete!")

