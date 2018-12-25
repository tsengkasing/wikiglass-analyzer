#!/usr/bin/env python3
import re
from html.parser import HTMLParser

"""
Usage:

text = "<p>Testing</p>\n''hello''\n'''world'''"
text = TextExtracter.trim(text)
# text = Testinghelloworld
"""

class TextExtracter:
    def __init__(self, text):
        self.text = text
    # Trim HTML
    def trim_html(self):
        parser = CustomHTMLParser()
        parser.feed(self.text.strip())
        self.text =parser.get_text()
    # Trim Spaces
    def trim_space(self):
        self.text = re.sub(r'\s', repl='', string=self.text, count=0, flags=re.M)
    # Trim DSL
    def trim_editor_marker(self):
        # trim overstriking
        self.text = re.sub(r"'''(.*)'''", repl=lambda m: m.group(1), string=self.text, count=0)
        # trim italic
        self.text = re.sub(r"''(.*)''", repl=lambda m: m.group(1), string=self.text, count=0)
        # trim second-level title
        self.text = re.sub(r"==(.*)==", repl=lambda m: m.group(1), string=self.text, count=0)
        # trim timestamp-signature
        self.text = re.sub(r"--\[\[.*UTC[（）()]{1}", repl='', string=self.text, count=0)
        # trim REDIRECT
        self.text = re.sub(r"#REDIRECT \[\[.*\]\]", repl='', string=self.text, count=0)
        # trim table
        self.text = re.sub(r'{| class="wikitable"(.*)|}', repl='', string=self.text, count=0, flags=re.M)
    '''
    Trim input string
    @param {string} text
    @return {string} trimmed text
    '''
    @staticmethod
    def trim(text):
        e = TextExtracter(text)
        e.trim_html()
        e.trim_editor_marker()
        e.trim_space()
        return e.text

class CustomHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
    # Process HTML & append text content to @var{fed}
    def handle_data(self, data):
        self.fed.append(data)
    def get_text(self):
        return ''.join(self.fed)
