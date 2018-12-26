#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List, Tuple
import numpy as np
import os, sys
import re
import dill
from .config_reader import ConfigReader

class SentenceClassifier(object):
    def __init__(self):
        # Read Config to get Model Location
        configreader = ConfigReader()
        model_dir = configreader.get('localsettings', 'SENTENCE_QUALITY_MODEL', 'model_dir')
        # Load Classifier Model
        with open("{}models.pkl".format(model_dir), 'rb') as in_file:
            models = dill.load(in_file)

        self.clf = models["classifier"]
        self.bow_ex = models["bow_extractor"]
        self.length_ex = models["length_extractor"]
        self.selected_features = models["selected_features"]

    # Implement singleton pattern with __new__
    def __new__(cls, *args, **kwargs):
        if not hasattr(SentenceClassifier, "_instance"):
            SentenceClassifier._instance = object.__new__(cls)
        return SentenceClassifier._instance

    @staticmethod
    def split_paragraph(paragraph: str) -> List[str]:
        """
        Split paragraph to sentences
        @param {String} paragraph utf-8 String
        @returns {String[]} utf-8 Strings List
        """
        sentence_split_pattern = "[。？?！!]"
        split_res = re.split(sentence_split_pattern, paragraph)
        return [sent for sent in split_res if len(sent) > 0]

    @staticmethod
    def clean_sentence(text: str):
        return re.sub(r'\s', '', text).strip()

    def classify_text(self, raw_text: str) -> List[Tuple[str, str]]:
        paragraph = SentenceClassifier.clean_sentence(raw_text)
        sentences = [sent for sent in SentenceClassifier.split_paragraph(paragraph)]
        bow_feats = self.bow_ex.extract(sentences)[0]
        length_feat = np.array(self.length_ex.extract(sentences)[0], dtype=np.int).reshape(-1,1)
        all_features = np.concatenate((bow_feats, length_feat), axis=1)
        res = []
        for idx, label in enumerate(self.clf.predict(all_features[:,self.selected_features])):
            if label == 1:
                res.append((sentences[idx],'level 1'))
            if label == 2:
                res.append((sentences[idx],'level 2'))
            if label == 3:
                res.append((sentences[idx],'level 3'))
        return res
