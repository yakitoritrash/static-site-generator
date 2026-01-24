from typing import Text
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link
from delimiter import split_nodes_delimiter
def text_to_textnodes(text):
    #This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
    #output: [
   # TextNode("This is ", TextType.TEXT),
   # TextNode("text", TextType.BOLD),
   # TextNode(" with an ", TextType.TEXT),
   # TextNode("italic", TextType.ITALIC),
   # TextNode(" word and a ", TextType.TEXT),
   # TextNode("code block", TextType.CODE),
   # TextNode(" and an ", TextType.TEXT),
   # TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
   # TextNode(" and a ", TextType.TEXT),
   # TextNode("link", TextType.LINK, "https://boot.dev"),
   # ]
   nodes = [TextNode(text, TextType.TEXT)]
   nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
   nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
   nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
   nodes = split_nodes_image(nodes)
   nodes = split_nodes_link(nodes)
   return (nodes)
