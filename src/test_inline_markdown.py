import unittest
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
                [TextNode("This is text with a ", TextType.TEXT),
                 TextNode("bolded phrase", TextType.BOLD),
                 TextNode(" in the middle", TextType.TEXT)
                 ],
                new_nodes,
                )

    def test_delim_bold_double(self):
        node = TextNode("This is text with a **bolded phrase** and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
                [TextNode("This is text with a ", TextType.TEXT),
                 TextNode("bolded phrase", TextType.BOLD),
                 TextNode(" and ", TextType.TEXT),
                 TextNode("another", TextType.BOLD)
                 ],
                new_nodes,
                )

    def test_delim_italic(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
                [TextNode("This is ", TextType.TEXT),
                 TextNode("italic", TextType.ITALIC),
                 TextNode(" text", TextType.TEXT),
                 ],
                new_nodes,
                )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
                [TextNode("This is text with a ", TextType.TEXT),
                 TextNode("code block", TextType.CODE),
                 TextNode(" word", TextType.TEXT),
                 ],
                new_nodes,
                )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
                [
                    TextNode("bold", TextType.BOLD),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC)
                    ], new_nodes
                )

    def test_delim_no_close(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()
