from antlr4 import *
from grammars.GOLDParser import GOLDParser
from grammars.GOLDParserVisitor import GOLDParserVisitor


class GOLDParserBaseVisitor(GOLDParserVisitor):
    tabs = 0

    def visitDescription(self, ctx: GOLDParser.DescriptionContext):
        for desc_block in ctx.blocks:
            self.visit(desc_block)

        return None

    def visitDescriptionBlock(self, ctx: GOLDParser.DescriptionBlockContext):
        name: Token = ctx.name
        print("Visiting description block " + "<" + name.text + ">")
        self.tabs += 1
        self.visit(ctx.headerBlock())
        self.visit(ctx.bodyBlock())
        self.tabs -= 1

    def visitHeaderBlock(self, ctx: GOLDParser.HeaderBlockContext):
        print("\t" * self.tabs + "Visiting header block")

        self.tabs += 1
        for languageBlock in ctx.lblocks:
            self.visit(languageBlock)
        self.tabs -= 1

    def visitLanguageBlock(self, ctx: GOLDParser.LanguageBlockContext):
        language_name: Token = ctx.langname
        print("\t" * self.tabs + "Visiting language block " + "<" + language_name.text + ">")
        self.tabs += 1
        self.visit(ctx.filesBlock())
        self.visit(ctx.typesBlock())
        self.tabs -= 1

    def visitFilesBlock(self, ctx: GOLDParser.FilesBlockContext):
        print("\t" * self.tabs + "Visiting files block")
        self.tabs += 1
        for file in ctx.files:
            self.visit(file)
        self.tabs -= 1

    def visitFile(self, ctx: GOLDParser.FileContext):
        name: Token = ctx.filename
        line: Token = ctx.line
        column: Token = ctx.column

        print("\t" * self.tabs + "Visiting file " + "<" + name.text + ":l" + line.text + ":c" + column.text + ">")

    def visitTypesBlock(self, ctx: GOLDParser.TypesBlockContext):
        print("\t" * self.tabs + "Visiting types block")
        self.tabs += 1
        for t in ctx.types:
            self.visit(t)
        self.tabs -= 1

    def visitType(self, ctx: GOLDParser.TypeContext):
        given_name: Token = ctx.goldtype
        orig_name: Token = ctx.langtype
        print("\t" * self.tabs + "Type " + given_name.text + " -> " + orig_name.text)

    def visitBodyBlock(self, ctx: GOLDParser.BodyBlockContext):
        print("\t" * self.tabs + "Visiting body block")
        self.tabs += 1
        for constant in ctx.constants:
            self.visit(constant)
        self.tabs -= 1

    def visitCommonConst(self, ctx: GOLDParser.CommonConstContext):
        type_id: Token = ctx.typeId
        var_name: Token = ctx.varName
        var_value: Token = ctx.varValue
        print("\t" * self.tabs + type_id.text + " " + var_name.text + " = " + var_value.text)
