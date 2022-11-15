# Import built-in modules
import os


def get_psd_files():
    this_root = os.path.dirname(__file__)
    file_root = os.path.join(this_root, "files")
    return {
        file_name: os.path.join(file_root, file_name)
        for file_name in os.listdir(file_root)
    }
