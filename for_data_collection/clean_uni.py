import re

def remove_bidirectional_unicode(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()

    # Define a regular expression pattern to match bidirectional Unicode text
    bidirectional_pattern = re.compile(r'[\u200e\u200f\u202a-\u202e\u2066-\u2069\ufb50-\ufdff\ufe70-\ufeff]')

    # Remove bidirectional Unicode characters from the text
    cleaned_text = re.sub(bidirectional_pattern, '', text)

    # Write the cleaned text to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_text)

# Usage
input_file = '_chat.txt'
output_file = 'cleaned_chat.txt'
remove_bidirectional_unicode(input_file, output_file)
