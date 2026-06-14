import re


SECTION_HEADERS = [
    "SUMMARY",
    "EXPERIENCE",
    "EDUCATION",
    "PROJECTS",
    "SKILLS",
    "LANGUAGES",
    "CERTIFICATIONS",
    "ACHIEVEMENTS"
]


def clean_resume_text(text):

    # Remove excessive whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    text = text.replace( "KEY ACHIEVEMENTS","\nKEY ACHIEVEMENTS\n")

    text = text.replace("PROJECTS SUMMARY","\nPROJECTS\nSUMMARY\n")

    # Force common headers onto new lines
    for header in SECTION_HEADERS:

        text = text.replace(
            f" {header}",
            f"\n{header}"
        )

    # Put bullet points on separate lines
    text = text.replace(
        "•",
        "\n•"
    )

    return text.strip()