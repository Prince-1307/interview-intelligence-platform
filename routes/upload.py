from flask import (
    Blueprint,
    render_template,
    request
)

import os

from config import (
    UPLOAD_FOLDER,
    ALLOWED_EXTENSIONS
)

from models.resume_parser import (
    extract_resume_text
)

from models.text_cleaner import (
    clean_resume_text
)

from models.skill_extractor import (
    load_skills,
    extract_skills
)

from models.question_generator import (
    load_question_bank,
    generate_questions
)

upload_bp = Blueprint(
    "upload",
    __name__
)


def allowed_file(filename):

    return (
        "." in filename
        and
        filename.rsplit(
            ".",
            1
        )[1].lower()
        in ALLOWED_EXTENSIONS
    )


@upload_bp.route(
    "/upload",
    methods=["GET", "POST"]
)
def upload_resume():

    success = False

    error = None

    resume_text = None

    detected_skills = []

    generated_questions = []

    if request.method == "POST":

        file = request.files.get(
            "resume"
        )

        # -----------------------
        # No file selected
        # -----------------------

        if not file or file.filename == "":

            error = "Please select a file."

        # -----------------------
        # Invalid file type
        # -----------------------

        elif not allowed_file(
            file.filename
        ):

            error = (
                "Only PDF and DOCX files are allowed."
            )

        # -----------------------
        # Valid file
        # -----------------------

        else:

            os.makedirs(
                UPLOAD_FOLDER,
                exist_ok=True
            )

            save_path = os.path.join(
                UPLOAD_FOLDER,
                file.filename
            )

            file.save(
                save_path
            )

            try:

                # -----------------------
                # Resume Parsing
                # -----------------------

                resume_text = extract_resume_text(
                    save_path
                )

                # -----------------------
                # Text Cleaning
                # -----------------------

                resume_text = clean_resume_text(
                    resume_text
                )

                # -----------------------
                # Skill Extraction
                # -----------------------

                skills_db = load_skills(
                    "data/skills.txt"
                )

                detected_skills = extract_skills(
                    resume_text,
                    skills_db
                )

                # -----------------------
                # Question Generation
                # -----------------------

                question_bank = load_question_bank(
                    "data/question_bank.json"
                )

                generated_questions = generate_questions(
                    detected_skills,
                    question_bank,
                    difficulty="medium"
                )

                success = True

            except Exception as e:

                error = (
                    f"Error parsing resume: {str(e)}"
                )

    return render_template(
        "upload.html",

        success=success,

        error=error,

        resume_text=resume_text,

        detected_skills=detected_skills,

        generated_questions=generated_questions
    )