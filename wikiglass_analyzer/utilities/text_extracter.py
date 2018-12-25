#!/usr/bin/env python3
import re
from html.parser import HTMLParser

"""
Usage:

text = "<p>Testing</p>\n''hello''\n'''world'''"
length = TextExtracter.len(text)
# word_list = ['Testing', 'hello', 'world']
# length = 3
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
    def trim(self):
        self.trim_html()
        self.trim_editor_marker()
        return self.text
    @staticmethod
    def valid(char):
        if char == '|':
            return False
        elif char == '!':
            return False
        elif char == '|-':
            return False
        return True
    @staticmethod
    def len(text):
        e = TextExtracter(text)
        word_list = e.trim().split( )
        word_list = [word for word in word_list if TextExtracter.valid(word)]
        return len(word_list)

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
