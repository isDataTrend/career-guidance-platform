from services.transcript_parser import parse_pdf

def test_parse_pdf():
    test_file = "tests/sample_transcript.pdf"
    result = parse_pdf(test_file)
    assert isinstance(result, str)
    assert "Expected Text" in result

