import os
import pandas as pd
import pdfplumber

def parse_transcript(filepath):
    """
    Parses a transcript file (CSV or PDF) to extract course and grade information.

    Args:
        filepath (str): Path to the transcript file.

    Returns:
        list: A list of courses with optional grades or extracted text.
    """
    file_extension = os.path.splitext(filepath)[1].lower()

    if file_extension == '.csv':
        return parse_csv(filepath)
    elif file_extension == '.pdf':
        return parse_pdf(filepath)
    else:
        raise ValueError("Unsupported file format. Only CSV and PDF are allowed.")

def parse_csv(filepath):
    """
    Parses a CSV file containing courses and grades.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        list: A list of courses extracted from the CSV.
    """
    df = pd.read_csv(filepath)
    if "Course" not in df.columns:
        raise ValueError("CSV file must have a 'Course' column.")
    return df["Course"].tolist()

def parse_pdf(filepath):
    """
    Extracts text from a PDF file and attempts to parse courses and grades.

    Args:
        filepath (str): Path to the PDF file.

    Returns:
        list: A list of courses or text lines from the PDF.
    """
    courses = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                courses.extend(lines)

    # Attempt to filter course-related text (optional based on your use case)
    # Example: Assume courses contain specific keywords like "Grade" or "Course"
    filtered_courses = [line for line in courses if "course" in line.lower() or "grade" in line.lower()]

    return filtered_courses if filtered_courses else courses

