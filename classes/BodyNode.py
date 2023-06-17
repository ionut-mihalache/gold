from abstract_classes.Visitor import Visitor
from classes.Node import Node


class BodyNode(Node):

    def __init__(self, definitions):
        if definitions is None:
            definitions = []
        self.__definitions = definitions

    def get_definitions(self):
        return self.__definitions

    def accept(self, visitor: Visitor):
        return visitor.visit_body_node(self)
