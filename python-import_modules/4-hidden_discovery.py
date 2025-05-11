#!/usr/bin/python3
import importlib.util
import sys
import os

def main():
    module_path = "/tmp/hidden_4.pyc"
    module_name = "hidden_4"

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = [name for name in dir(module) if not name.startswith("__")]
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    main()

