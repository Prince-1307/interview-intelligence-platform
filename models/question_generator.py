import json


def load_question_bank(filepath):

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )


def generate_questions(
    skills,
    question_bank,
    difficulty="medium"
):

    questions = []

    for skill in skills:

        if skill in question_bank:

            questions.extend(
                question_bank[skill].get(
                    difficulty,
                    []
                )
            )

    return questions