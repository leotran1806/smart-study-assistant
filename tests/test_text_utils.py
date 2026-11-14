import unittest
import os
import sys

import text_utils as utils

class TestFunctions(unittest.TestCase):
    def test_basic(self):
        with self.subTest("Basic"):
            output = utils.normalize_text("  Hello   World   ")
            self.assertNotEndsWith(output, ' ')
        with self.subTest("A little trickier"):
            output = utils.normalize_text("Hello\nWorld")
            self.assertEqual(output, "Hello World")
        
    def test_with_tab_char(self):
        self.maxDiff = None
        output = utils.normalize_text('  \t  "Hello, world!" -- said John-Paul.  \t  \n'
            'Is this a state-of-the-art, 100% accurate system?  \n'
            '\t  \n'
            '  Email: user.test+1@sub.domain.co.uk ...  Cost: $1,234.56 / 50.5%  \n'
            'Wait... what?!   No\xa0way--yes\u200bway!  \n'
            '\n'
            '  \n'
            'Final line without trailing newline.  ')
        self.assertEqual(output, '"Hello, world!" -- said John-Paul. '
            'Is this a state-of-the-art, 100% accurate system? '
            'Email: user.test+1@sub.domain.co.uk ... Cost: $1,234.56 / 50.5% '
            'Wait... what?! No way--yes\u200bway! '
            'Final line without trailing newline.')
    
    def test_words_count_for_normalized_text_basic(self):
        text = " Hello how are you \x0f"
        self.assertEqual(utils.words_count_for_normalized_text(utils.normalize_text(text)), 5)
        
    def test_words_count_for_normalized_text_medium(self):
        text = """Hệ thống đang tiến hành đọc dữ liệu từ tệp văn bản. 
                Yêu cầu kiểm tra lại định dạng dòng và ký tự xuống dòng (CRLF hoặc LF) trước khi phân tích cú pháp.
                Chúc bạn hoàn thành tốt bài tập lập trình!"""
        self.assertTrue(utils.words_count_for_normalized_text(utils.normalize_text(text)) == 43)
        
    def test_document_analyze_basic(self):
        path_name = './documents/log1.txt'
        result = {"filename": './documents/log1.txt',
                  "wordcount": 35,
                  "charcount": 100}
        self.assertFalse(utils.document_Analyze(path_name) == result)
        
    def test_document_analyze_non_existing_file(self):
        path_name = './documents/log12.txt'
        self.assertRaises(FileNotFoundError)
        
if __name__ == "__main__":
    unittest.main()

