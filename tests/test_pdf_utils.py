import unittest
import pdf_utils as utils

class TestFunctions(unittest.TestCase):
    def test_reading_pdf_1_page(self):
        file_path = "./documents/test1.pdf"
        result = utils.extract_text_from_pdf(file_path)
        self.assertEqual(len(result), 1)
    
    def test_reading_pdf_with_no_reading_permission(self):
        file_path = "./documents/no_permission.pdf"
        result = utils.extract_text_from_pdf(file_path)
        self.assertRaises(PermissionError)
        
    def test_reading_empty_pdf(self):
        file_path = "./documents/empty.pdf"
        result = utils.extract_text_from_pdf(file_path)
        with self.subTest("Page counting"):   
            self.assertEqual(result[0].get("page"), 1)
        
        with self.subTest("Data checking"):
            self.assertFalse(result[0].get("data"), "")
            
if __name__ == "__main__":
    unittest.main()