import sys
from antlr4 import *

from classes.DescriptionNode import DescriptionNode
from grammars.gen.GOLDLexer import GOLDLexer
from grammars.gen.GOLDParser import GOLDParser
from visitors.GOLDParserBaseVisitor import GOLDParserBaseVisitor
from visitors.GenerationVisitor import GenerationVisitor
from visitors.PrintVisitor import PrintVisitor

DESCRIPTION_DIR = "descriptions"

def get_parser(filename):
    input_stream = FileStream(filename)
    lexer = GOLDLexer(input_stream)
    stream = CommonTokenStream(lexer)

    return GOLDParser(stream)


def main():
    argc: int = len(sys.argv)
    if len(sys.argv) < 1:
        print("Not enough command line parameters.")
        print("At least description file should be provided.")
        print("<python> gold.py <file1_path>.gold <file2_path>.gold ...")
        exit(1)

    for i in range(1, argc):
        parser = get_parser(DESCRIPTION_DIR + "/" + sys.argv[i])
        tree = parser.description()
        base_visitor = GOLDParserBaseVisitor()
        root_node: DescriptionNode = base_visitor.visit(tree)

        print_visitor = PrintVisitor()
        generation_visitor = GenerationVisitor()

        root_node.accept(print_visitor)
        root_node.accept(generation_visitor)


if __name__ == "__main__":
    main()
