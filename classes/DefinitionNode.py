from abc import abstractmethod

from abstract_classes.Visitor import Visitor
from classes.Node import Node


class DefinitionNode(Node):

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass
