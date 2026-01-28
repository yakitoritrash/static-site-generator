import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_withtitle(self):
        s = """
# this is a markdown with a title
<this is a paragraph in it.
"""
        self.assertEqual(extract_title(s), "this is a markdown with a title")
    def test_withmultitpletitle(self):
        s = """
# this is a markdown with a title
## this is another markdown with a title
<this is a paragraph in it.
"""
        self.assertEqual(extract_title(s), "this is a markdown with a title")
    def test_notitle(self):
        with self.assertRaises(ValueError):
            extract_title("""
## this is another markdown with a title
<this is a paragraph in it.
""")

if __name__ == "__main__":
    unittest.main()
