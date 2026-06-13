from flask import Blueprint
from flask import render_template
from flask import request

import os

from config import (
    UPLOAD_FOLDER,
    ALLOWED_EXTENSIONS
)

upload_bp = Blueprint("upload",__name__)


def allowed_file(filename):

    return ("." in filename and filename.rsplit(".", 1 )[1].lower() in ALLOWED_EXTENSIONS )


@upload_bp.route(
    "/upload",
    methods=["GET", "POST"]
)
def upload_resume():

    success = False
    error = None

    if request.method == "POST":

        file = request.files.get(
            "resume"
        )

        if not file:

            error = "No file selected."

        elif not allowed_file(
            file.filename
        ):

            error = (
                "Only PDF and DOCX files are allowed."
            )

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

            success = True

    return render_template(
        "upload.html",
        success=success,
        error=error
    )