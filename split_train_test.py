"""usage:
    python split_train_test.py --root=path/to/folder/root/
"""
from pathlib import Path
import random
import shutil


def split(root_name):
    root_path = Path(root_name)
    for char_dir in root_path.iterdir():
        train_dir = root_path / 'train'
        test_dir = root_path / 'test'

        train_dir.mkdir()
        test_dir.mkdir()

        for file_path in random.sample(list(char_dir.iterdir()), 80):
            *_, file_name = file_path.parts
            shutil.move(file_path, train_dir / file_name)

        for file_path in char_dir.iterdir():
            *_, file_name = file_path.parts
            shutil.move(file_path, test_dir / file_name)

        shutil.move(train_dir, char_dir)
        shutil.move(test_dir, char_dir)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=str)
    args = parser.parse_args()

    split(args.root)
