from abstract_classes.Visitor import Visitor
from classes.Node import Node


class TypeNode(Node):

    def __init__(self, given_name, orig_name):
        self.__given_name = given_name
        self.__orig_name = orig_name

    def get_given_name(self) -> str:
        return self.__given_name

    def get_orig_name(self) -> str:
        return self.__orig_name

    def accept(self, visitor: Visitor):
        return visitor.visit_type_node(self)
