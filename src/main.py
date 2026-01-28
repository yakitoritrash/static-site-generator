from os import stat
from textnode import TextNode, TextType
from statictopub import copy_files_recursive, static_to_public
from generate_path import generate_page
from generate_pages_recursive import generate_pages_recursive
def main():

    static_to_public()
    generate_pages_recursive("content", "template.html", "public")
    #dummy_node = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")

main()
