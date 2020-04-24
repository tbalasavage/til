import argparse
import os
from pathlib import Path


parser = argparse.ArgumentParser("new_til.py")
parser.add_argument("category", help="Category of TIL", type=str)
parser.add_argument("title", help="Title of TIL", type=str)
args = parser.parse_args()

category_lower = args.category.lower()
category_lower_underscores = category_lower.replace(" ", "_")
title_lower = args.title.lower()

if not os.path.exists(category_lower):
    print(f'* [{args.category}](#{category_lower.replace(" ", "-")})')
    print(f'### {args.category}')
    os.mkdir(category_lower_underscores)

title_with_underscores = title_lower.replace(" ", "_")
file_path = os.path.join(category_lower_underscores, title_with_underscores + ".md")
if not os.path.exists(file_path):
    Path(file_path).touch()
    print(f'* [{args.title}]({file_path})')
    