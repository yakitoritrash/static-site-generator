import os
from pathlib import Path
from generate_path import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, dest_path)
        elif os.path.isfile(from_path) and filename.endswith(".md"):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
