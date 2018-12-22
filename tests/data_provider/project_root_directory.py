import sys, os

def project_root_dir():
    cwd = os.getcwd()
    parent_dir = os.path.dirname(cwd)
    grand_parent_dir = os.path.dirname(parent_dir)
    sys.path.append(grand_parent_dir)

project_root_dir()