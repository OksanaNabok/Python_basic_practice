import re

def capitalize_after_punctuation(text):
    """Capitalize the first alphabetic character following any '.!? ' or at the start of a new line."""
    return re.sub(r'([.!?]\s+|\A\s*)(\w)', lambda m: m.group(1) + m.group(2).upper(), text)

# Initialize the homework paragraph
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

# Reduce multiple newlines to a single newline and normalize to lower case
normalized_text = re.sub(r'\n+', '\n', homework_text.strip()).lower()

# Correctly fixing 'iz' to 'is' only when it occurs as a distinct word
corrected_text = re.sub(r'\biz\b', 'is', normalized_text)

# Capitalize after each ending punctuation and at the start
final_text = capitalize_after_punctuation(corrected_text)

# Collect the last words of each sentence to form the new sentence
last_words = re.findall(r'\b\w+\b(?=[.!?])', final_text)
new_sentence = ' '.join(last_words).capitalize() + '.'

# Append the new sentence to the existing sentences in the final text
final_text += ' ' + new_sentence

# Calculate the number of whitespace characters
whitespace_count = sum(c.isspace() for c in final_text)

# Print results
print("Normalized and corrected text:")
print(final_text)
print("\nNumber of whitespace characters:", whitespace_count)