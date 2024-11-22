import pdfplumber

def parse_transcript(filepath, filetype):
    if filetype == "pdf":
        return parse_pdf(filepath)
    elif filetype == "csv":
        return parse_csv(filepath)
    else:
        raise ValueError("Unsupported file type")

def parse_pdf(filepath):
    with pdfplumber.open(filepath) as pdf:
        return "".join(page.extract_text() for page in pdf.pages)

def parse_csv(filepath):
    # Add logic for parsing CSV files if needed
    return "Sample CSV Parsing Logic"

