# Error Records and Methodology applied

## 19/10/2026:
1. Function directoryAnalyze() calls function reportWrite() with wrong indentation -> fix indentation
2. Initial version of textNormalize() cannot resolve some kind of unwanted unicode format characters like BOM (\ufeff) or \u200b (zero-width Space)
    * Solution: integrate python library: "unicodedata" -> check if the category is not "Cf" (other format) type, then it is allowed in processed text.