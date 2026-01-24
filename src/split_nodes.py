from extract_markdown import extract_markdown_images
from extract_markdown import extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        matches = extract_markdown_images(original_text)
        #matches = [('image', 'https://i.imgur.com/zjjcJKZ.png'), ('second image', 'https://i.imgur.com/3elNhQu.png')]
        if len(matches) == 0:
            new_nodes.append(old_node)
            continue
        for image_alt, image_link in matches:
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return (new_nodes)
            

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        matches = extract_markdown_links(original_text)
        if len(matches) == 0:
            new_nodes.append(old_node)
            continue
        for link_addr, link in matches:
            sections = original_text.split(f"[{link_addr}]({link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_addr, TextType.LINK, link))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return (new_nodes);


