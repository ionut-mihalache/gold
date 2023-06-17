from abstract_classes.Visitor import Visitor
from classes.Node import Node


class FileNode(Node):

    def __init__(self, name, line, column):
        self.__name = name
        self.__line = line
        self.__column = column

    def get_name(self) -> str:
        return self.__name

    def get_line(self) -> int:
        return self.__line

    def get_column(self) -> int:
        return self.__column

    def accept(self, visitor: Visitor):
        return visitor.visit_file_node(self)
