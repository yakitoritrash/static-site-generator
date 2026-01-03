from textnode import TextNode, TextType
def main():
    dummy_node = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")
    print(dummy_node)

main()


