"""Calculate JSON pointers with their source location for each value of a YAML document."""

import pathlib

import yaml


def calculate():
    """Calculate the YAML source map."""
    with open(pathlib.Path(__file__).parent / "test.yaml") as in_file:
        loader = yaml.Loader(in_file)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token().end_mark)
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
        print(loader.get_token())
        print(loader.pointer)
