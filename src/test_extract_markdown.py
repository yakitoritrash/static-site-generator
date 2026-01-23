import unittest
from extract_markdown import extract_markdown_images 
from extract_markdown import extract_markdown_links

class TestExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
                )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links("This is a text with a [link](https://www.youtube.com/watch?v=asm7YUwWLzg)")
        self.assertListEqual([("link", "https://www.youtube.com/watch?v=asm7YUwWLzg")], matches)
