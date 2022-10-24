#!/usr/local/bin/python3
from datetime import datetime
import os
import argparse
import shutil

argparse = argparse.ArgumentParser()
argparse.add_argument(
    "--dry",
    help="Dry run, nothing will be deleted",
    required=False,
    action="store_true"
)

args, pathes = argparse.parse_known_args()


def check_if_to_keep(path):
    # get name of folder from path
    basename = os.path.basename(path)
    # check if basename matches date format %Y-%m-%d
    try:
        basename_date = datetime.strptime(basename, '%Y-%m-%d')
    except ValueError:
        return False

    # get current date
    current_date = datetime.now()
    # check if basename is equal or grater than to current date
    if basename_date >= current_date:
        return True
    else:
        return False


if __name__ == '__main__':
    if type(pathes) is list:
        for path in pathes:
            path = os.path.expanduser(path)
            # raise error if path is a file or does not exist
            if os.path.isfile(path):
                raise Exception(f"{path} is a file, not a directory")
            elif not os.path.exists(path):
                raise Exception(f'{path} does not exist')
            # check every subfolder in path
            # list all subfolders in path with absolute path
            subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
            for subfolder in subfolders:
                if os.path.isdir(subfolder) or os.path.isfile(subfolder):
                    if check_if_to_keep(subfolder):
                        print(f"keep: {subfolder}")
                    else:
                        print(f"delete: {subfolder}")
                        # if argument dry set to false then delete file or folder
                        if not args.dry:
                            pass
                            shutil.rmtree(subfolder)