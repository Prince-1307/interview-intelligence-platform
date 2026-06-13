from flask import (Blueprint, render_template, request)

import os

from config import ( UPLOAD_FOLDER, ALLOWED_EXTENSIONS
)

from models.resume_parser import (
    extract_resume_text
)

upload_bp = Blueprint("upload", __name__)


def allowed_file(filename):
    """
    Check whether uploaded file
    has a valid extension.
    """

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

    if request.method == "POST":

        file = request.files.get(
            "resume"
        )

        # --------------------------
        # No file selected
        # --------------------------

        if not file or file.filename == "":

            error = "Please select a file."

        # --------------------------
        # Invalid file type
        # --------------------------

        elif not allowed_file(
            file.filename
        ):

            error = (
                "Only PDF and DOCX files are allowed."
            )

        # --------------------------
        # Valid file
        # --------------------------

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

                resume_text = (
                    extract_resume_text(
                        save_path
                    )
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
        resume_text=resume_text
    )