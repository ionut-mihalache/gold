from abstract_classes.Visitor import Visitor
from classes.FileNode import FileNode
from classes.Node import Node


class FilesNode(Node):

    def __init__(self, files):
        if files is None:
            files = []
        self.__files: list[FileNode] = files

    def get_files(self):
        return self.__files

    def accept(self, visitor: Visitor):
        return visitor.visit_files_node(self)
