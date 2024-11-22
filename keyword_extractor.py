import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(skills):
    keywords = []
    for skill in skills:
        doc = nlp(skill)
        keywords.extend([token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']])
    return list(set(keywords))

