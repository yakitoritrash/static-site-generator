import unittest
from block_to_blocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        block = "###### This is a h6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        # Edge case: No space after # is NOT a heading
        block = "#NoSpace"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        block = "```\ncode block\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote\n> It spans multiple lines"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        # Edge case: One line missing the >
        block = "> This is a quote\nBut this line breaks it"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        block = "* Item 1\n* Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        block = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        # Edge case: No space
        block = "*NoSpace"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        # Edge case: Starts with wrong number
        block = "2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Edge case: Out of order
        block = "1. First\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        block = "Just a normal paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
