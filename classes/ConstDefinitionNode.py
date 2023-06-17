from abstract_classes.Visitor import Visitor
from classes.DefinitionNode import DefinitionNode


class ConstDefinitionNode(DefinitionNode):

    def __init__(self, type_id, name, value):
        self.__type_id = type_id
        self.__name = name
        self.__value = value
        super().__init__()

    def get_type(self):
        return self.__type_id

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

    def accept(self, visitor: Visitor):
        return visitor.visit_definition_node(self)
