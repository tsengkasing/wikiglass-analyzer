#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from wikiglass_analyzer.utilities.text_extracter import TextExtracter

class TestTextExtracter(unittest.TestCase):
    def test_html(self):
        l = TextExtracter.len("<p>Hello World</p>")
        self.assertEqual(l, 2)

    def test_Chinese(self):
        l = TextExtracter.len("<p>測試中文</p>")
        self.assertEqual(l, 4)

    def test_overstriking(self):
        l = TextExtracter.len("'''world'''")
        self.assertEqual(l, 1)

    def test_italic(self):
        l = TextExtracter.len("\n''Hello''\n")
        self.assertEqual(l, 1)

    def test_secondary_title(self):
        l = TextExtracter.len("==二級標題==")
        self.assertEqual(l, 4)

    def test_mixed(self):
        text = """
        這是一個測試頁面。
        '''加粗'''
        ''斜体''
        <s>删除线</s>

        ==二级标题==


        <gallery>
        檔案:圖片.jpg|標題
        檔案:圖片.jpg|標題
        </gallery>

        --[[用戶:Everstar|Everstar]]（[[用戶討論:Everstar|討論]]） 2018年12月24日 (一) 13:18 (UTC)

        #REDIRECT [[重新導向]]

        <!-- 隱藏評論 -->

        [https://www.google.com.hk 谷歌]

        <bs:blog />

        {| class="wikitable"
        |-
        ! 標題 1
        ! 標題 2
        ! 標題 3
        |-
        | 列 1, 儲存格 1
        | 列 1, 儲存格 2
        | 列 1, 儲存格 3
        |-
        | 列 2, 儲存格 1
        | 列 2, 儲存格 2
        | 列 2, 儲存格 3
        |}

        <audio style="display: none;" controls="controls"></audio>

        <audio style="display: none;" controls="controls"></audio>
        """
        l = TextExtracter.len(text)
        self.assertEqual(l, 93)
