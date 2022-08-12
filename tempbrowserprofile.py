#!/usr/bin/python3

"""
tempbrowserprofile - open a browser with a temporary profile

(c) 2022 Bruno Oberle (https://boberle.com) - MIT license
"""

import argparse
import tempfile
import os
import shutil
import subprocess

__version__ = "2.0.0"


DEFAULT_EXECUTABLE = "firefox"
DEFAULT_OPTION = "profile"


def parse_args():
    parser = argparse.ArgumentParser(
        prog="tempbrowserprofile",
        description="open a browser with a temporary profile",
    )
    parser.add_argument(
        "-e", "--executable",
        default=DEFAULT_EXECUTABLE,
        help="command or executable to run the browser. "
        f"Default is '{DEFAULT_EXECUTABLE}'",
    )
    parser.add_argument(
        "-o", "--profile-option",
        help="profile option to use with the executable."
        f"Default for '{DEFAULT_EXECUTABLE}' is '{DEFAULT_OPTION}'."
        "End with '=' to get an option of the format '--option=value'",
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
            args.executable,
        ]
        if args.profile_option and args.profile_option.endswith("="):
            cmd.append(f'--{args.profile_option}{tmp}')
        elif args.profile_option:
            cmd.extend([f'--{args.profile_option}', tmp])
        print(f"Opening '{args.executable}' with profile in '{tmp}'.")
        print(cmd)
        subprocess.run(cmd)


if __name__ == "__main__":
    main()
