import sys
from antlr4 import *
from grammars.GOLDLexer import GOLDLexer
from grammars.GOLDParser import GOLDParser
from visitors.GOLDParserBaseVisitor import GOLDParserBaseVisitor


def get_parser(filename):
    input_stream = FileStream(filename)
    lexer = GOLDLexer(input_stream)
    stream = CommonTokenStream(lexer)

    return GOLDParser(stream)


def main():
    parser = get_parser(sys.argv[1])
    tree = parser.description()
    visitor = GOLDParserBaseVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    main()
