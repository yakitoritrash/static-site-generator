import os
import shutil

def static_to_public():
    src_dir = './static'
    dest_dir = './public'

    print("Deleting public directory...")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    print("Copying static files to public directory...")
    copy_files_recursive(src_dir, dest_dir)

def copy_files_recursive(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    for s in os.listdir(source_path):
        from_path = os.path.join(source_path, s)
        to_path = os.path.join(destination_path, s)
        print(f" * Copying {from_path} -> {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files_recursive(from_path, to_path)
    #print(os.path.exists('./static'))
    #print(os.listdir('./static'))
    #print(os.path.join('./static', 'x'))
    #os.path.isfile("./static")
