antlr=java -jar antlr/antlr-4.13.0-complete.jar

.PHONY: build clean

build:
	$(antlr) -Dlanguage=Python3 -visitor -no-listener grammars/GOLDLexer.g4
	$(antlr) -Dlanguage=Python3 -visitor -no-listener grammars/GOLDParser.g4

run:
	python3 gold.py $(FILE)

clean:
	rm grammars/*.interp grammars/*.tokens grammars/GOLDLexer.py grammars/GOLDParser.py grammars/GOLDParserVisitor.py
