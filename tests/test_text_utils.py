import unittest
import os
import sys

# Lấy đường dẫn thư mục hiện tại của file test.py (parent_folder)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Lấy đường dẫn thư mục cha của nó (D:\Coding_Project\Python_project)
parent_dir = os.path.dirname(current_dir)

# Thêm thư mục gốc vào sys.path để Python nhận diện được utils_folder
sys.path.append(parent_dir)
import text_utils as utils

class TestNormalizeText(unittest.TestCase):
    
    def test_basic(self):
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
if __name__ == "__main__":
    unittest.main()

