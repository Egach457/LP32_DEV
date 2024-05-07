import os
import tempfile


def create_custom_temp_dir():
    custom_temp_dir_path = os.path.abspath(os.path.dirname(__file__))
    temp_dir = tempfile.mkdtemp(dir=custom_temp_dir_path)
    return temp_dir
