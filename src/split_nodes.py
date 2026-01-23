from extract_markdown import extract_markdown_images
from extract_markdown import extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.TextType != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        original_text = old_node.text
        matches = extract_markdown_images(original_text)
        if len(matches) == 0:
            new_nodes.append(old_nodes)
            continue
        for image_alt, image_link in matches:
            sections = old_nodes.text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            

def split_nodes_link(old_nodes):
    matches = extract_markdown_links(old_nodes.text)
    new_nodes = []
    if matches == []:
        new_nodes.append(old_nodes)


node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )

split_nodes_image(node)
