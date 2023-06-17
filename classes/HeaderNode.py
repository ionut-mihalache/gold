from abstract_classes.Visitor import Visitor
from classes.LanguageNode import LanguageNode
from classes.Node import Node


class HeaderNode(Node):

    def __init__(self, languages):
        if languages is None:
            languages = []
        self.__languages: list[LanguageNode] = languages

    def get_languages(self):
        return self.__languages

    def accept(self, visitor: Visitor):
        visitor.visit_header_node(self)
