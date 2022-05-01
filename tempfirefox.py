#!/usr/bin/python3

"""
tempfirefox - open Firefox with a temporary profile

(c) 2022 Bruno Oberle (https://boberle.com) - MIT license
"""

import argparse
import tempfile
import os
import shutil
import subprocess


DEFAULT_FIREFOX_EXECUTABLE = "firefox"


def parse_args():
    parser = argparse.ArgumentParser(
        prog="tempfirefox",
        description="open firefox with a temporary profile",
    )
    parser.add_argument(
        "-f", "--firefox-executable",
        default=DEFAULT_FIREFOX_EXECUTABLE,
        help="command or executable to run firefox. Default is 'firefox'",
    )
    parser.add_argument(
        "-p", "--default-profile",
        help="default profile directory to start with",
    )
    args = parser.parse_args()
    return args


def copy_default_profile(src, dst):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        if os.path.isdir(src_path):
            dst_path = os.path.join(dst, item)
            shutil.copytree(src_path, dst_path)
        else:
            shutil.copy(src_path, dst)


def main():
    args = parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        if args.default_profile:
            print(
                f"Copying default profile '{args.default_profile}' to '{tmp}'"
            )
            copy_default_profile(args.default_profile, tmp)
        cmd = [
            args.firefox_executable,
            '--profile',
            tmp,
        ]
        print(f"Opening Firefox with profile in '{tmp}'.")
        subprocess.run(cmd)


if __name__ == "__main__":
    main()
