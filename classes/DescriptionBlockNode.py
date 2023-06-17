from abstract_classes.Visitor import Visitor
from classes.Node import Node


class DescriptionBlockNode(Node):

    def __init__(self, name, header_node, body_node):
        self.__name = name
        self.__header_node = header_node
        self.__body_node = body_node

    def get_name(self):
        return self.__name

    def get_header_node(self):
        return self.__header_node

    def get_body_node(self):
        return self.__body_node

    def accept(self, visitor: Visitor):
        return visitor.visit_description_block_node(self)
