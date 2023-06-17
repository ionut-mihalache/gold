from abstract_classes.Visitor import Visitor
from classes.Node import Node


class LanguageNode(Node):

    def __init__(self, name, files_node, types_node):
        if files_node is None:
            files_node = []
        if types_node is None:
            types_node = []

        self.__name = name
        self.__files_node = files_node
        self.__types_node = types_node

    def get_name(self):
        return self.__name

    def get_files_node(self):
        return self.__files_node

    def get_types_node(self):
        return self.__types_node

    def accept(self, visitor: Visitor):
        return visitor.visit_language_node(self)
