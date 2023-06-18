from antlr4 import *

from classes.BodyNode import BodyNode
from classes.ConstDefinitionNode import ConstDefinitionNode
from classes.DescriptionNode import DescriptionNode
from classes.DescriptionBlockNode import DescriptionBlockNode
from classes.FileNode import FileNode
from classes.FilesNode import FilesNode
from classes.HeaderNode import HeaderNode
from classes.LanguageNode import LanguageNode
from classes.TypeNode import TypeNode
from classes.TypesNode import TypesNode
from grammars.GOLDParser import GOLDParser
from grammars.GOLDParserVisitor import GOLDParserVisitor


class GOLDParserBaseVisitor(GOLDParserVisitor):
    __body_node = None

    def visitDescription(self, ctx: GOLDParser.DescriptionContext):
        descriptions: list = []

        for desc_block in ctx.blocks:
            descriptions.append(self.visit(desc_block))

        return DescriptionNode(descriptions)

    def visitDescriptionBlock(self, ctx: GOLDParser.DescriptionBlockContext):
        name: Token = ctx.name

        body_node = self.visit(ctx.bodyBlock())
        self.__body_node = body_node
        header_node = self.visit(ctx.headerBlock())

        return DescriptionBlockNode(name.text, header_node)

    def visitHeaderBlock(self, ctx: GOLDParser.HeaderBlockContext):
        languages: list[LanguageNode] = []

        for languageBlock in ctx.lblocks:
            languages.append(self.visit(languageBlock))

        return HeaderNode(languages)

    def visitLanguageBlock(self, ctx: GOLDParser.LanguageBlockContext):
        language_name: Token = ctx.langname

        files_node = self.visit(ctx.filesBlock())
        types_node = self.visit(ctx.typesBlock())

        return LanguageNode(language_name.text, files_node, types_node, self.__body_node)

    def visitFilesBlock(self, ctx: GOLDParser.FilesBlockContext):
        files: list[FileNode] = []

        for file in ctx.files:
            files.append(self.visit(file))

        return FilesNode(files)

    def visitFile(self, ctx: GOLDParser.FileContext):
        name: Token = ctx.filename
        line: Token = ctx.line
        column: Token = ctx.column

        return FileNode(name.text, int(line.text), int(column.text))

    def visitTypesBlock(self, ctx: GOLDParser.TypesBlockContext):
        types: list[TypeNode] = []

        for t in ctx.types:
            types.append(self.visit(t))

        return TypesNode(types)

    def visitType(self, ctx: GOLDParser.TypeContext):
        given_name: Token = ctx.goldtype
        orig_name: Token = ctx.langtype

        return TypeNode(given_name.text, orig_name.text[2:-1])

    def visitBodyBlock(self, ctx: GOLDParser.BodyBlockContext):
        definitions = []

        for constant in ctx.constants:
            definitions.append(self.visit(constant))

        return BodyNode(definitions)

    def visitCommonConst(self, ctx: GOLDParser.CommonConstContext):
        type_id: Token = ctx.typeId
        var_name: Token = ctx.varName
        var_value: Token = ctx.varValue

        return ConstDefinitionNode(type_id.text, var_name.text, var_value.text[2:-1])
