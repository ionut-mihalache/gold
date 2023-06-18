from abstract_classes.Visitor import Visitor
from classes.BodyNode import BodyNode
from classes.FilesNode import FilesNode
from classes.Node import Node
from classes.TypeNode import TypeNode
from classes.TypesNode import TypesNode


class LanguageNode(Node):

    def __init__(self, name, files_node, types_node, body_node):
        if files_node is None:
            raise Exception("files_node cannot be null")
        if types_node is None:
            raise Exception("types_node cannot be null")
        if body_node is None:
            raise Exception("body_node cannot be null")

        self.__name: str = name
        self.__files_node: FilesNode = files_node
        self.__types_node: TypesNode = types_node
        self.__body_node: BodyNode = body_node

    def get_name(self):
        return self.__name

    def get_files_node(self):
        return self.__files_node

    def get_types_node(self):
        return self.__types_node

    def get_body_node(self):
        return self.__body_node

    def lookup_type_id(self, type_id):
        types: list[TypeNode] = self.__types_node.get_types()

        for t in types:
            if t.get_given_name() == type_id:
                return t

        return None

    def accept(self, visitor: Visitor):
        return visitor.visit_language_node(self)
