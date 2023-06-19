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


class GenerationVisitor(Visitor, ABC):

    def __init__(self):
        self.__curr_language_node: LanguageNode | None = None
        self.__code_lines: list[str] | None = None

    def visit_description_node(self, node: DescriptionNode):
        for block in node.get_description_blocks():
            self.visit_description_block_node(block)

    def visit_description_block_node(self, node: DescriptionBlockNode):
        self.visit_header_node(node.get_header_node())

    def visit_header_node(self, node: HeaderNode):
        for language in node.get_languages():
            self.visit_language_node(language)

    def visit_language_node(self, node: LanguageNode):
        self.__curr_language_node = node

        self.__code_lines = self.visit_body_node(node.get_body_node())
        self.visit_files_node(node.get_files_node())
        self.__code_lines = None

    def visit_files_node(self, node: FilesNode):
        for file in node.get_files():
            self.visit_file_node(file)

    def visit_file_node(self, node: FileNode):
        if self.__code_lines is None:
            return

        with open(node.get_name(), "r+") as f:
            f_lines = f.readlines()

            self.__code_lines.reverse()
            for line in self.__code_lines:
                f_lines.insert(node.get_line(), " " * node.get_column() + line + "\n")

            # set cursor back at the start of the file
            f.seek(0)

            f.writelines(f_lines)

    def visit_types_node(self, node: TypesNode):
        pass

    def visit_type_node(self, node: TypeNode):
        pass

    def visit_body_node(self, node: BodyNode):
        res: list[str] = []
        for definition in node.get_definitions():
            res.append(self.visit_definition_node(definition))

        return res

    def visit_definition_node(self, node):
        if type(node) is ConstDefinitionNode:
            return self.__visit_const_node(node)

    def __visit_const_node(self, node: ConstDefinitionNode):
        curr_lang_node = self.__curr_language_node
        if curr_lang_node is None:
            return ""

        language = curr_lang_node.get_name()
        definition_type: TypeNode = self.__curr_language_node.lookup_type_id(node.get_type())

        if language == "php":
            return definition_type.get_orig_name() + " " + node.get_name() + " = " + node.get_value() + ";"
        elif language == "js":
            return node.get_name() + " = " + node.get_value() + ";"
        else:
            print(language + " generation not supported")
