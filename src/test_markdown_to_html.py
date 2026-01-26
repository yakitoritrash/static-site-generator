import unittest
from htmlnode import HTMLNode
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        # Align this to the far left!
        md = """```
This is text that _should_ remain the **same**
even with inline stuff
```"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><pre><code>This is text that <i>should</i> remain the <b>same</b>\neven with inline stuff</code></pre></div>"
        self.assertEqual(html, expected)

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an ordered list
2. with items
3. and more items
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an ordered list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

## this is an h2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote></div>",
        )

if __name__ == "__main__":
    unittest.main()
