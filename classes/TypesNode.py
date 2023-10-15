from abstract_classes.Visitor import Visitor
from classes.Node import Node
from classes.TypeNode import TypeNode


class TypesNode(Node):

    def __init__(self, types):
        self.__types: list[TypeNode] = types

    def get_types(self):
        return self.__types

    def accept(self, visitor: Visitor):
        return visitor.visit_types_node(self)
