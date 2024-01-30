# Write a program that extracts a title and all the content of a HTML file:
# •	The title should be between the HTML tags <title> and <\title>.
# •	The content should be between the HTML tags <body> and <\body>.
# There might be different HTML tags, which you should ignore:
# •	Each HTML tag is surrounded by the symbols "<" and ">". For example: <body>, <p>, <\html>
# •	You also should ignore the HTML tag "\n"
# Example:
# "<html>\n<head><title>News</title></head>\n<body><p><a href="https://softuni.bg">SoftUni</a>aims to provide free real-world practical\n training for young people who want to turn into\n skillful Python software engineers.</p></body>\n</html>"
# In this example the title is "News" and the content is "SoftUni aims to provide free real-world practical training for young people who want to turn into skillful Python software engineers."
# Input
# •	The input will be read from the console.
# •	The input consists of a single line.
# Output
# •	The content should be a single string.
# •	You should extract only the text without the tags.
# •	When you extract the title and the content, you should print the result in the following format:
# o	"Title: {extracted title}"
# o	"Content: {extracted content}"

import re
from html.parser import HTMLParser


text = input()

title_pattern = r'<title>(.+)<\/title>'
extracted_title = ''.join(re.findall(title_pattern, text))

content_pattern = r'<body>(.+)<\/body>'
extracted_content = re.findall(content_pattern,text)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
parser.handle_data(extracted_content)

# print(f"Title: {extracted_title}")
# print(f"Content: {content_pattern}")