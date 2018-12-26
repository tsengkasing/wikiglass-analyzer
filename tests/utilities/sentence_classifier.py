#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import path, environ
import unittest
from wikiglass_analyzer.utilities.sentence_classifier import SentenceClassifier

class TestSentenceClassifier(unittest.TestCase):
    def setUp(self):
        # Mock Configuration File
        environ['WIKIGLASS_LOCALSETTINGS_PATH'] = path.normpath(
            "{}/../../localsettings.ini.example".format(
                path.dirname(path.realpath(__file__))
            )
        )
        self.classifier = SentenceClassifier()

    def test_level_1(self):
        text = '沒有人知道的地方'
        result = self.classifier.classify_text(text)
        sentence, level = result[0]
        self.assertEqual(text, sentence)
        self.assertEqual(level, 'level 1')

    def test_level_2(self):
        text = '這是一句普通的話語'
        result = self.classifier.classify_text(text)
        sentence, level = result[0]
        self.assertEqual(text, sentence)
        self.assertEqual(level, 'level 2')

    def test_level_3(self):
        text = '要改變這種現狀，就需要提倡健康的傳統飲食'
        result = self.classifier.classify_text(text)
        sentence, level = result[0]
        self.assertEqual(text, sentence)
        self.assertEqual(level, 'level 3')

    def test_paragraph(self):
        text = '''
        在這次專題探究搜集的虐待動物案件之中，我更加了觧到現時虐待動物的情況。
        現時的人對虐待動物的看灋龢虐待動物者對動物的看灋，我對此感到非常憤怒。
        那羣虐動物者竟然認爲動物是一件翫具，他們竟然當一箇生命是翫具，令我拾分憤慨！
        '''
        result = self.classifier.classify_text(text)
        self.assertEqual(len(result), 3)
        for _, level in result:
            self.assertEqual(level, 'level 2')
