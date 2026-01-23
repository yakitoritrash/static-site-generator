import re

def extract_markdown_images(text):
    #"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text);
    return matches

def extract_markdown_links(text):
    #text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    matches = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text);
    return matches
