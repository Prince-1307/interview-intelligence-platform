import re


def clean_resume_text(text):

    text = re.sub(r"\s+"," ",text)

    text = text.replace("•","\n•")

    text = text.replace(" EXPERIENCE","\nEXPERIENCE")

    text = text.replace(" EDUCATION","\nEDUCATION")

    text = text.replace( " LANGUAGES","\nLANGUAGES")
    
    return text.strip()