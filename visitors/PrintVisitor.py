from abc import ABC

from abstract_classes.Visitor import Visitor
from classes.BodyNode import BodyNode
from classes.ConstDefinitionNode import ConstDefinitionNode
from classes.DescriptionBlockNode import DescriptionBlockNode
from classes.DescriptionNode import DescriptionNode
from classes.FileNode import FileNode
from classes.FilesNode import FilesNode
from classes.HeaderNode import HeaderNode
from classes.LanguageNode import LanguageNode
from classes.TypeNode import TypeNode
from classes.TypesNode import TypesNode


class PrintVisitor(Visitor, ABC):

    def __init__(self):
        self.__tabs = 0
        self.__curr_language_node: LanguageNode | None = None

    def visit_description_node(self, node: DescriptionNode):
        for block in node.get_description_blocks():
            self.visit_description_block_node(block)

    def visit_description_block_node(self, node: DescriptionBlockNode):
        print("Visiting description block " + "<" + node.get_name() + ">")
        self.visit_header_node(node.get_header_node())

    def visit_header_node(self, node: HeaderNode):
        self.__tabs += 1
        for language in node.get_languages():
            self.visit_language_node(language)
        self.__tabs -= 1

    def visit_language_node(self, node: LanguageNode):
        print("\t" * self.__tabs + "Visiting language block " + "<" + node.get_name() + ">")
        self.__curr_language_node = node
        self.__tabs += 1
        self.visit_files_node(node.get_files_node())
        self.visit_types_node(node.get_types_node())
        self.visit_body_node(node.get_body_node())
        self.__tabs -= 1

    def visit_files_node(self, node: FilesNode):
        print("\t" * self.__tabs + "Visiting files block")
        self.__tabs += 1
        for fileNode in node.get_files():
            self.visit_file_node(fileNode)
        self.__tabs -= 1

    def visit_file_node(self, node: FileNode):
        print("\t" * self.__tabs + "file: " +
              node.get_name() + ":l" + str(node.get_line()) + ":c" + str(node.get_column()))

    def visit_types_node(self, node: TypesNode):
        print("\t" * self.__tabs + "Visiting types block")
        self.__tabs += 1
        for file in node.get_types():
            self.visit_type_node(file)
        self.__tabs -= 1

    def visit_type_node(self, node: TypeNode):
        if node.get_orig_name() != "":
            print("\t" * self.__tabs + "Type " + node.get_given_name() + " -> " + node.get_orig_name())

    def visit_body_node(self, node: BodyNode):
        print("\t" * self.__tabs + "Visiting body block")
        self.__tabs += 1
        for definition in node.get_definitions():
            self.visit_definition_node(definition)
        self.__tabs -= 1

    def visit_definition_node(self, node):
        if type(node) is ConstDefinitionNode:
            self.__visit_const_node(node)

    def __visit_const_node(self, node: ConstDefinitionNode):
        if self.__curr_language_node is None:
            return
        definition_type: TypeNode = self.__curr_language_node.lookup_type_id(node.get_type())
        print("\t" * self.__tabs +
              ((definition_type.get_orig_name() + " ") if definition_type.get_orig_name() != "" else "")
              + node.get_name() + " = " + node.get_value())
