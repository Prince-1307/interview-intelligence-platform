SECTION_HEADERS = [
    "SUMMARY",
    "EXPERIENCE",
    "EDUCATION",
    "PROJECTS",
    "SKILLS",
    "LANGUAGES",
    "CERTIFICATIONS"
]


def structure_resume(text):

    sections = {}

    current_section = "other"

    sections[current_section] = []

    lines = text.split("\n")

    for line in lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        upper_line = clean_line.upper()

        if upper_line in SECTION_HEADERS:

            current_section = upper_line.lower()

            sections[current_section] = []

        else:

            sections[current_section].append(
                clean_line
            )

    cleaned_sections = {}

    for key, value in sections.items():

        section_text = "\n".join(value).strip()

        if section_text:

            cleaned_sections[key] = (section_text)

    return cleaned_sections