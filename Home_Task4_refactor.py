import re

def normalize_whitespace(text):
    """Reduce multiple newlines to a single newline and strip unnecessary spaces."""
    return re.sub(r'\n+', '\n', text.strip()).lower()

def correct_mistakes(text):
    """Correct specific misspellings and grammar issues."""
    return re.sub(r'\biz\b', 'is', text)

def capitalize_after_punctuation(text):
    """Capitalize the first alphabetic character following any '.!? ' or at the start of a new line."""
    return re.sub(r'([.!?]\s+|\A\s*)(\w)', lambda m: m.group(1) + m.group(2).upper(), text)

def append_new_sentence(text):
    """Append a new sentence formed from the last words of existing sentences."""
    last_words = re.findall(r'\b\w+\b(?=[.!?])', text)
    new_sentence = ' '.join(last_words).capitalize() + '.'
    return text + ' ' + new_sentence

def count_whitespace(text):
    """Count the number of whitespace characters in the text."""
    return sum(c.isspace() for c in text)

def process_text(text):
    """Process the given text through all stages of corrections and adjustments."""
    normalized = normalize_whitespace(text)
    corrected = correct_mistakes(normalized)
    capitalized = capitalize_after_punctuation(corrected)
    final_text = append_new_sentence(capitalized)
    return final_text, count_whitespace(final_text)

# Homework text
homework_text = (
    "\n"
    "HomEwork:\n"
    "\n"
    " tHis iz your homeWork, copy these text to variable.\n"
    "\n"
    "\n"
    "\n"
    " You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE "
    "sEnTENCE witH LAST WoRDS of each existING sentence and add it to the END of this paragraph.\n"
    "\n"
    "\n"
    "\n"
    "it iZ misspelling here. fix“iZ” with correct “is”, but ONLY when it is a mistAKE.\n"
    "\n"
    "\n"
    "\n"
    "last iz TO calculate number of whitespace characters in this Tex. Carefull, not "
    "only spaces, but all whitespaces. I Got 87.\n"
)

# Execute text processing
final_text, whitespace_count = process_text(homework_text)

# Print results
print("Normalized and corrected text:")
print(final_text)
print("\nNumber of whitespace characters:", whitespace_count)