import os
import shutil
from textnode import TextNode, TextType
from statictopub import copy_files_recursive, static_to_public
from generate_path import generate_page
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    dest_dir = "docs"

    print(f"Cleaning {dest_dir} directory...")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    print(f"Copying static files to {dest_dir} directory...")
    copy_files_recursive("static", dest_dir)
    print("Generating content...")
    
    generate_pages_recursive("content", "template.html", dest_dir, basepath)
    #dummy_node = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")

main()
