# Text Extracter

## Introduction

In order to count the number of words in a page, we need to extract the pure text content from the Rich Text.

Consider the following situation :arrow_down:

![DSL](https://user-images.githubusercontent.com/10103993/50403170-5e1f8d80-07d7-11e9-91d0-10cfb75fc9da.png)

There are some different markers that we want to trim.
- HTML Tags `</> &nbsp;`
- Editor Markers
  - overstriking `'''overstriking_text'''`
  - italic `''italic_text''`
  - Secondary Title `==Title==`
  - Redirect `#REDIRECT [[text]]`
  - ...
- Spaces & Line Break

## Question

- Q: Are there any packages that can be used to count the words ?
- A: Nope. We are counting both Chinese characters & alphanumeric characters, we can simply use `len()` function in **Python** . However, we need to extract the pure text first.

## Method

- HTML Tags
  For **HTML** contents, we use **HTMLParser** which is provided natively.
- Editor Markers
  For DSL(Domain Specific Language) Markers, we can only replace them one by one using Regular Expression.
- Spaces & Line break
  We can remove spaces & Line Break using Regular Expression.
