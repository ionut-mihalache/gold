from abstract_classes.Visitor import Visitor
from classes.Node import Node


class FileNode(Node):

    def __init__(self, name, start_block, end_block):
        self.__name = name
        self.__start_block = start_block
        self.__end_block = end_block

    def get_name(self) -> str:
        return self.__name

    def get_start_block(self) -> str:
        return self.__start_block

    def get_end_block(self) -> str:
        return self.__end_block

    def accept(self, visitor: Visitor):
        return visitor.visit_file_node(self)
