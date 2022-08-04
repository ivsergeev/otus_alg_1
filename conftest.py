# -*- coding: utf-8 -*-
from os import getcwd, listdir
from os.path import exists, join

ARGS = ["input", "output"]
IN_EXT = ".in"
OUT_EXT = ".out"

def pytest_addoption(parser):
    parser.addoption("--folder", action="store", help="Path to OTUS test files")

def pytest_generate_tests(metafunc):
    if all(x in metafunc.fixturenames for x in ARGS):
        path = join(getcwd(), metafunc.config.getoption("folder") or "fixtures") 
        inputs = [file for file in listdir(path) if file.endswith(IN_EXT)]
        inputs.sort()
        cases = []
        for input in inputs:
            output = input[:-len(IN_EXT)] + OUT_EXT
            input_path = join(path, input)
            output_path = join(path, output) 
            if exists(output_path):
                with open(input_path) as fin:
                    input_val = int(fin.readline())
                with open(output_path) as fout:
                    output_val = int(fout.readline())
                cases.append((input_val, output_val))
        metafunc.parametrize(",".join(ARGS), cases)
