import sys
from antlr4 import *

from classes.DescriptionNode import DescriptionNode
from grammars.GOLDLexer import GOLDLexer
from grammars.GOLDParser import GOLDParser
from visitors.GOLDParserBaseVisitor import GOLDParserBaseVisitor
from visitors.GenerationVisitor import GenerationVisitor
from visitors.PrintVisitor import PrintVisitor


def get_parser(filename):
    input_stream = FileStream(filename)
    lexer = GOLDLexer(input_stream)
    stream = CommonTokenStream(lexer)

    return GOLDParser(stream)


def main():
    parser = get_parser(sys.argv[1])
    tree = parser.description()
    base_visitor = GOLDParserBaseVisitor()
    root_node: DescriptionNode = base_visitor.visit(tree)

    print_visitor = PrintVisitor()
    generation_visitor = GenerationVisitor()

    root_node.accept(print_visitor)
    root_node.accept(generation_visitor)


if __name__ == "__main__":
    main()
