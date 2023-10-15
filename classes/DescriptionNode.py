from abstract_classes.Visitor import Visitor
from classes.Node import Node


class DescriptionNode(Node):

    def __init__(self, description_blocks=None):
        if description_blocks is None:
            description_blocks = []

        self.__descriptionBlocks = description_blocks

    def get_description_blocks(self) -> list:
        return self.__descriptionBlocks

    def accept(self, visitor: Visitor):
        return visitor.visit_description_node(self)
