import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
                "div",
                "Hello, world!",
                None,
                {"class": "greeting", "href": "https://boot.dev"},
                )
        self.assertEqual(
                node.props_to_html(),
                ' class = "greeting" href = "https://boot.dev"',
                )
    def test_values(self):
        node = HTMLNode(
                "div",
                "I wish I could read"
                )
        self.assertEqual(
                node.tag,
                "div",
                )
        self.assertEqual(
                node.value,
                "I wish I could read"
                )

        self.assertEqual(
                node.children,
                None,
                )

        self.assertEqual(
                node.props,
                None,
                )

    def test_repr(self):
        node = HTMLNode(
                "p",
                "What a strange world",
                None,
                {"class": "primary"}
                )
                
        self.assertEqual(
                node.__repr__(),
                "HTMLNode(p, What a strange world, None, {'class': 'primary'})"
                )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_props(self):
        node = LeafNode("a", "click me", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href = "https://google.com">click me</a>')
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")
    def test_leaf_to_html_no_value_raises_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
if __name__ == "__main__":
    unittest.main()
