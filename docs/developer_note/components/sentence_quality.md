# Sentence Quality

## Classifier Model

The Classifier Model File is ``assets/sentence_quality_model/models.pkl``

## Classifier Information

### Input

Text Paragraph

### Output

Type: ``List[Tuple[str, str]]``

A **list**, with each element is a **tuple**. Each **tuple** consist of TWO strings, one is a sentence while the other is the **level**.

Input Text Paragraph will be splitted into several sentences and classify one by one. Absolutely, Output List will only consist of ONE element if the input is ONE sentence.

## Classifier Usage

```python
from wikiglass_analyzer.utilities.sentence_classifier import SentenceClassifier

classifier = SentenceClassifier()

text = '要改變這種現狀，就需要提倡健康的傳統飲食'
result = classifier.classify_text(text)
sentence, level = result[0]

# sentence = '要改變這種現狀，就需要提倡健康的傳統飲食'
# level = 'level 3'
```
