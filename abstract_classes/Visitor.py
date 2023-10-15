from __future__ import annotations
from abc import abstractmethod


class Visitor:
    @abstractmethod
    def visit_description_node(self, node):
        pass

    @abstractmethod
    def visit_description_block_node(self, node):
        pass

    @abstractmethod
    def visit_header_node(self, node):
        pass

    @abstractmethod
    def visit_language_node(self, node):
        pass

    @abstractmethod
    def visit_files_node(self, node):
        pass

    @abstractmethod
    def visit_file_node(self, node):
        pass

    @abstractmethod
    def visit_types_node(self, node):
        pass

    @abstractmethod
    def visit_type_node(self, node):
        pass

    @abstractmethod
    def visit_body_node(self, node):
        pass

    @abstractmethod
    def visit_definition_node(self, node):
        pass
