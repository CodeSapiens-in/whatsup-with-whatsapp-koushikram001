import re

# Define a regular expression pattern to match strings between "]" and ":"
name_pattern = r'\] (.*?):'
f = open("demofile2.txt", "a" ,encoding='utf-8', errors='ignore' )


# Open and read the chat log text file
with open('cleaned_chat.txt', 'r', encoding='utf-8') as file:
    chat_log = file.read()

# Use regular expression to find all matches of strings
strings_between_brackets = re.findall(name_pattern, chat_log)

# Print the extracted strings
for string in strings_between_brackets:
    print(string)
    f.write(string + "\n")
f.close()
