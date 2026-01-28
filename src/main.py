from os import stat
from textnode import TextNode, TextType
from statictopub import copy_files_recursive, static_to_public
def main():

    static_to_public()
    #dummy_node = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")

main()
