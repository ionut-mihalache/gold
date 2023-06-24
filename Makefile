antlr=java -jar antlr/antlr-4.13.0-complete.jar
antlr_options=-Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir
grammars_dir=grammars
grammars_output_dir=$(grammars_dir)/gen/

.PHONY: build clean

build:
	$(antlr) $(antlr_options) $(grammars_dir)/GOLDLexer.g4 -o $(grammars_output_dir)
	$(antlr) $(antlr_options) $(grammars_dir)/GOLDParser.g4 -lib $(grammars_output_dir) -o $(grammars_output_dir)

run:
	python3 gold.py $(FILE)

clean:
	rm -rf $(grammars_output_dir)
