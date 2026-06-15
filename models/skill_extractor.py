def load_skills(filepath):

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as file:

        skills = [

            line.strip()

            for line in file.readlines()

            if line.strip()

        ]

    return skills


def extract_skills(
    text,
    skill_list
):

    text = text.lower()

    found_skills = []

    for skill in skill_list:

        if skill.lower() in text:

            found_skills.append(
                skill
            )

    return sorted(
        list(
            set(
                found_skills
            )
        )
    )