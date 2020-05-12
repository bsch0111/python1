import sys

from cx_Freeze import setup, Executable



setup(  name = "parser",

        version = "1.0",

        description = "Parser",

        author = "sh1n2",

        executables = [Executable("SIFT_BFMatch.py")])  