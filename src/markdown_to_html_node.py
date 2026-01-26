from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    #blocks = ['This is **bolded** paragraph\ntext in a p\ntag here', 'This is another paragraph with _italic_ text and `code` here']
    for block in blocks:
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.PARAGRAPH:
            x = HTMLNode("")




md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

markdown_to_html_node(md)
