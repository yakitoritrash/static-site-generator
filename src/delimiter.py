from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_list = node.text.split(delimiter)
        if len(split_list) % 2 == 0:
            raise ValueError("Invalid delimiter")

        for i in range(len(split_list)):
            if split_list[i] == "":
                continue
            if i % 2 == 0:
                n = TextNode(split_list[i], TextType.TEXT)
                new_nodes.append(n)
            else:
                n = TextNode(split_list[i], text_type)
                new_nodes.append(n)
    return new_nodes
