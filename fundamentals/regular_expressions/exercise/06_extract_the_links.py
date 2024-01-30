# Write a program that extracts links from a given text.
# The text will come in the form of strings, each representing a sentence.
# You need to extract only the valid links from it. Example:
# The Sub-Domain must always be "www".
# The Domain name can consist of English alphabet letters (uppercase and lowercase), digits, and dashes ("–").
# The Domain extension consists of one or more domain blocks,
#   a domain block consists of a dot followed by one or more lowercase English alphabet letters,
#   a Domain extension must have at least one domain block in order to be valid.
# The Sub-Domain and Domain name must be separated by a single dot.
# Any link that does NOT follow the specified above rules should be treated as invalid.
import re

while True:
    givven_text = input()

    if givven_text:
        pattern = r'\b(([w]{3}.)([a-zA-Z0-9\-]+)(\.[a-z]+)+)\b'
        found_link = re.search(pattern, givven_text)
        if found_link:
            print(found_link.group())
    else:
        break

